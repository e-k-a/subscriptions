from sqlalchemy.ext.asyncio import AsyncSession
from src.models.models import Payment
from src.schemas.schemas import PaymentCreate,PaymentResponse
from sqlalchemy.future import select
from typing import Optional

# Создание платежа
async def create_payment(db: AsyncSession, user_id: int, amount: float, subscription_id: Optional[int] = None):
    payment = Payment(user_id=user_id, amount=amount, subscription_id=subscription_id)
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    return payment

async def get_payment(db: AsyncSession, payment_id: int):
    result = await db.execute(select(PaymentResponse).filter(Payment.id == payment_id))
    return result.scalars().first()

async def get_all_payments(db: AsyncSession):
    result = await db.execute(select(PaymentResponse))
    return result.scalars().all()


