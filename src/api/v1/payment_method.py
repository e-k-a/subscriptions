
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud import payment_methods
from src.schemas.schemas import PaymentMethodResponse, PaymentMethodCreate
from src.db.postgres import get_session

router = APIRouter()


@router.get("/payment-methods/{payment_method_id}", response_model=PaymentMethodResponse)
async def get_payment_method(payment_method_id: int, db: AsyncSession = Depends(get_session)):
    payment_method = await payment_methods.get_payment_method(db=db, payment_method_id=payment_method_id)
    if not payment_method:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return payment_method

@router.post("/payment-methods/", response_model=PaymentMethodResponse)
async def create_payment_method(payment_method: PaymentMethodCreate, db: AsyncSession = Depends(get_session)):
    return await payment_methods.create_payment_method(
        db=db,
        user_id=payment_method.user_id,
        card_number=payment_method.card_number,
        card_holder=payment_method.card_holder,
        expiry_date=payment_method.expiry_date,
        cvv=payment_method.cvv,
        balance = payment_method.balance,
        is_default=payment_method.is_default
    )

@router.put("/payment-methods/{payment_method_id}/default")
async def update_payment_method_default(user_id: int, payment_method_id: int, db: AsyncSession = Depends(get_session)):
    await payment_methods.update_default_payment_method(db=db, user_id=user_id, payment_method_id=payment_method_id)
    return {"message": "Default payment method updated"}