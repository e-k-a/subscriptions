from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from src.models.models import PaymentMethod


async def create_payment_method(
    db: AsyncSession,
    user_id: int,
    card_number: str,
    expiry_date: str,
    cvv: int,
    balance: float,
    is_default: bool,
):
    payment_method = PaymentMethod(
        user_id=user_id,
        card_number=card_number,
        expiry_date=expiry_date,
        cvv=cvv,
        balance=balance,
        is_default=is_default,
    )
    db.add(payment_method)
    await db.commit()
    await db.refresh(payment_method)
    return payment_method


async def get_payment_method(db: AsyncSession, payment_method_id: int):
    result = await db.execute(
        select(PaymentMethod).filter(PaymentMethod.id == payment_method_id)
    )
    return result.scalars().first()


async def get_all_payment_methods(db: AsyncSession):
    result = await db.execute(select(PaymentMethod))
    return result.scalars().all()


async def update_payment_method(
    db: AsyncSession, user_id: int, payment_method_id: int
):
    await db.execute(
        update(PaymentMethod)
        .where(PaymentMethod.user_id == user_id)
        .values(is_default=False)
    )
    await db.execute(
        update(PaymentMethod)
        .where(PaymentMethod.id == payment_method_id)
        .values(is_default=True)
    )
    await db.commit()


async def update_payment_method_balance(db: AsyncSession, user_id: int, amount: float):
    payment_method = await db.execute(
        select(PaymentMethod).filter(PaymentMethod.user_id == user_id)
    )
    payment_method = payment_method.scalars().first()
    if not payment_method:
        return None

    new_balance = payment_method.balance + amount
    await db.execute(
        update(PaymentMethod)
        .where(PaymentMethod.id == payment_method.id)
        .values(balance=new_balance)
    )
    await db.commit()

    result = await db.execute(
        select(PaymentMethod).filter(PaymentMethod.id == payment_method.id)
    )
    return result.scalars().first()