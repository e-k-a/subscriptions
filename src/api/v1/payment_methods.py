from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud import payment_method
from src.schemas.schemas import PaymentMethodResponse, PaymentMethodCreate
from src.db.postgres import get_session
from typing import List


router = APIRouter()

@router.get("/", response_model=List[PaymentMethodResponse])
async def get_all_payment_methods(db: AsyncSession = Depends(get_session)):
    return await payment_method.get_all_payment_methods(db=db)


@router.get("/{payment_method_id}", response_model=PaymentMethodResponse)
async def get_payment_method(
    payment_method_id: int, db: AsyncSession = Depends(get_session)
):
    payment_method_res = await payment_method.get_payment_method(
        db=db, payment_method_id=payment_method_id
    )
    if not payment_method_res:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return payment_method_res


@router.post("/", response_model=PaymentMethodResponse)
async def create_payment_method(
    payment_method_data: PaymentMethodCreate, db: AsyncSession = Depends(get_session)
):
    return await payment_method.create_payment_method(
        db=db,
        user_id=payment_method_data.user_id,
        card_number=payment_method_data.card_number,
        expiry_date=payment_method_data.expiry_date,
        cvv=payment_method_data.cvv,
        balance=payment_method_data.balance,
        is_default=payment_method_data.is_default,
    )


@router.put("/{payment_method_id}/default")
async def update_payment_method_default(
    user_id: int, payment_method_id: int, db: AsyncSession = Depends(get_session)
):
    return await payment_method.update_payment_method(
        db=db, user_id=user_id, payment_method_id=payment_method_id
    )
