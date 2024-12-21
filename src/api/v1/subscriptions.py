from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.schemas import SubscriptionResponse, SubscriptionCreate
from src.crud import subscription
from src.db.postgres import get_session

# from src.crud.subscription import create_subscription,get_subscription

router = APIRouter()


@router.post("/", response_model=SubscriptionResponse)
async def create_subscriptions(
    subscription_data: SubscriptionCreate, db: AsyncSession = Depends(get_session)
):
    return await subscription.create_subscription(
        db=db,
        user_id=subscription_data.user_id,
        name=subscription_data.name,
        price=subscription_data.price,
        duration_days=subscription_data.duration_days,
    )


@router.get("/{subscription_id}", response_model=SubscriptionResponse)
async def get_subscriptions(
    subscription_id: int, db: AsyncSession = Depends(get_session)
):
    subscription_data = await subscription.get_subscription(
        db=db, subscription_id=subscription_id
    )
    if not subscription_data:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription


@router.get("/user/{user_id}", response_model=list[SubscriptionResponse])
async def get_subscriptions_by_user(
    user_id: int, db: AsyncSession = Depends(get_session)
):
    return await subscription.get_subscriptions_by_user(db=db, user_id=user_id)


# Update the status of a subscription
@router.put("/{subscription_id}/status")
async def update_subscription_status(
    subscription_id: int, is_active: bool, db: AsyncSession = Depends(get_session)
):
    return await subscription.update_subscription_status(
        db=db, subscription_id=subscription_id, is_active=is_active
    )


@router.delete("/{subscription_id}")
async def delete_subscription(
    subscription_id: int, db: AsyncSession = Depends(get_session)
):
    deleted_subscription = await subscription.delete_subscription(db=db, subscription_id=subscription_id)
    if not deleted_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return deleted_subscription