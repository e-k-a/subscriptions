from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.models import Notification

async def create_notification(db: AsyncSession, user_id: int, message: str):
    notification = Notification(user_id=user_id, message=message)
    db.add(notification)
    await db.commit()
    await db.refresh(notification)
    return notification

async def get_notification(db: AsyncSession, notification_id: int):
    result = await db.execute(select(Notification).filter(Notification.id == notification_id))
    return result.scalars().first()

async def get_all_notifications(db: AsyncSession):
    result = await db.execute(select(Notification))
    return result.scalars().all()
