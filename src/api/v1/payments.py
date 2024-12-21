from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.postgres import get_session
from src.crud import payment, payment_method
from src.schemas.schemas import PaymentResponse, PaymentCreate

router = APIRouter()


@router.post("/", response_model=PaymentResponse)
async def create_payment(
    payment_data: PaymentCreate, db: AsyncSession = Depends(get_session)
):

    created_payment = await payment.create_payment(
        db=db,
        user_id=payment_data.user_id,
        amount=payment_data.amount,
        subscription_id=payment_data.subscription_id,
    )

    updated_payment_method = await payment_method.update_payment_method_balance(
        db=db,
        user_id=payment_data.user_id,
        amount=payment_data.amount,
    )
    if not updated_payment_method:
        raise HTTPException(status_code=404, detail="Payment method not found")

    return created_payment


# Get all payments
@router.get("/", response_model=list[PaymentResponse])
async def get_all_payments(db: AsyncSession = Depends(get_session)):
    
    return await payment.get_all_payments(db=db)
