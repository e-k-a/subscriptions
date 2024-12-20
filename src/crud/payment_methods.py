from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from src.models.models import PaymentMethod

async def create_payment_method(db: AsyncSession, user_id: int, card_number: str, card_holder: str, expiry_date: str, cvv: str, balance: float, is_default: bool):
    payment_method = PaymentMethod(user_id=user_id, card_number=card_number, card_holder=card_holder, expiry_date=expiry_date, cvv=cvv, balance=balance, is_default=is_default)
    db.add(payment_method)
    await db.commit()
    await db.refresh(payment_method)
    return payment_method

async def get_payment_method(db: AsyncSession, payment_method_id: int):
    result = await db.execute(select(PaymentMethod).filter(PaymentMethod.id == payment_method_id))
    return result.scalars().first()

async def get_all_payment_methods(db: AsyncSession):
    result = await db.execute(select(PaymentMethod))
    return result.scalars().all()

async def update_default_payment_method(db: AsyncSession, user_id: int, payment_method_id: int):
    await db.execute(update(PaymentMethod).where(PaymentMethod.user_id == user_id).values(is_default=False))
    await db.execute(update(PaymentMethod).where(PaymentMethod.id == payment_method_id).values(is_default=True))
    await db.commit()


    