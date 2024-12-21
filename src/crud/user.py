from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.models import User


async def create_users(db: AsyncSession, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    await db.commit()
    return user


async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


async def update_user(
    db: AsyncSession, user_id: int, name: str = None, email: str = None
):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return None
    if name:
        user.name = name
    if email:
        user.email = email
    await db.commit()
    await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user:
        await db.delete(user)
        await db.commit()
    return user
