from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from src.models.models import Subscription


# Create a new subscription
async def create_subscription(
    db: AsyncSession, user_id: int, name: str, price: float, duration_days: int
):
    expires_at = datetime.now() + timedelta(days=duration_days)
    subscription = Subscription(
        user_id=user_id, name=name, price=price, expires_at=expires_at, is_active=True
    )
    db.add(subscription)
    await db.commit()
    await db.refresh(subscription)
    return subscription


# Get a subscription by ID
async def get_subscription(db: AsyncSession, subscription_id: int):
    result = await db.execute(
        select(Subscription).filter(Subscription.id == subscription_id)
    )
    return result.scalars().first()


# Get all subscriptions for a specific user
async def get_subscriptions_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(Subscription).filter(Subscription.user_id == user_id)
    )
    return result.scalars().all()


# Update the status of a subscription
async def update_subscription_status(db: AsyncSession, subscription_id: int, is_active: bool):
    query = (
        update(Subscription)
        .where(Subscription.id == subscription_id)
        .values(is_active=is_active, updated_at=datetime.now())
    )
    await db.execute(query)
    await db.commit()


# Delete a subscription
async def delete_subscription(db: AsyncSession, subscription_id: int):
    await db.execute(
        delete(Subscription).where(Subscription.id == subscription_id)
    )
    await db.commit()