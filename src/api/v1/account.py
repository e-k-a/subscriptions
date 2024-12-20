
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.crud import account
from src.schemas.schemas import AccountResponse
from src.db.postgres import get_session

router = APIRouter()

@router.get("/accounts/{account_id}", response_model=AccountResponse)
async def get_account(account_id: int, db: AsyncSession = Depends(get_session)):
    account = await account.get_account(db=db, account_id=account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.put("/accounts/{account_id}/balance")
async def update_account_balance(account_id: int, balance: float, db: AsyncSession = Depends(get_session)):
    await account.update_account_balance(db=db, account_id=account_id, amount=balance)
    return {"message": "Account balance updated"}