from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.schemas import SubscriptionResponse, SubscriptionCreate
from src.crud import subscription
from src.db.postgres import get_session
from src.crud.subscription import create_subscription

router = APIRouter()


# Create a subscription
@router.post("/subscriptions/", response_model=SubscriptionResponse)
async def create_subscriptions(
    subscription: SubscriptionCreate, db: AsyncSession = Depends(get_session)
):
    return await create_subscription(
        db=db,
        user_id=subscription.user_id,
        name=subscription.name,
        price=subscription.price,
        duration_days=subscription.duration_days,
    )


# Get a subscription by ID
@router.get("/subscriptions/{subscription_id}", response_model=SubscriptionResponse)
async def get_subscription(subscription_id: int, db: AsyncSession = Depends(get_session)):
    subscription = await subscription.get_subscription(db=db, subscription_id=subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription


# Get all subscriptions for a user
@router.get("/subscriptions/user/{user_id}", response_model=list[SubscriptionResponse])
async def get_subscriptions_by_user(user_id: int, db: AsyncSession = Depends(get_session)):
    return await subscription.get_subscriptions_by_user(db=db, user_id=user_id)


# Update the status of a subscription
@router.patch("/subscriptions/{subscription_id}/status")
async def update_subscription_status(
    subscription_id: int, is_active: bool, db: AsyncSession = Depends(get_session)
):
    await subscription.update_subscription_status(
        db=db, subscription_id=subscription_id, is_active=is_active
    )
    return {"message": "Subscription status updated"}


@router.delete("/subscriptions/{subscription_id}")
async def delete_subscription(subscription_id: int, db: AsyncSession = Depends(get_session)):
    await subscription.delete_subscription(db=db, subscription_id=subscription_id)
    return {"message": "Subscription deleted"}