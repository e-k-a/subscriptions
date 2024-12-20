from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.postgres import get_session
from src.crud import payment
from src.schemas.schemas import PaymentResponse, PaymentCreate

router = APIRouter()


@router.post("/payments/", response_model=PaymentResponse)
async def create_payment(payment: PaymentCreate, db: AsyncSession = Depends(get_session)):
    # Create the payment
    created_payment = await payment.create_payment(
        db=db,
        user_id=payment.user_id,
        amount=payment.amount,
        subscription_id=payment.subscription_id,
    )

    # Update the balance of the payment method
    updated_payment_method = await payment.update_payment_method_balance(
        db=db,
        payment_method_id=payment.payment_method_id,
        amount=payment.amount,
    )
    if not updated_payment_method:
        raise HTTPException(status_code=404, detail="Payment method not found")

    return created_payment

# Get all payments
@router.get("/payments/", response_model=list[PaymentResponse])
async def get_all_payments(db: AsyncSession = Depends(get_session)):
    return await payment.get_all_payments(db=db)
