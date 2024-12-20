
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.crud import users
from src.schemas.schemas import UserCreate, UserResponse
from src.db.postgres import get_session

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    return await users.create_users(db=db, name=user.name, email=user.email)

# async def create_users(user: UserCreate, db: Session = Depends(get_session)):
#     return await create_users(db=db, name=user.name, email=user.email)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    db_user = await users.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    return await users.get_users(db=db, skip=skip, limit=limit)

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_session)):
    updated_user = await users.update_user(db=db, user_id=user_id, name=user.name, email=user.email)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session)):
    deleted_user = await users.delete_user(db=db, user_id=user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user