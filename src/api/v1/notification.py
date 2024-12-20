
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud import notification
from src.schemas.schemas import NotificationResponse, NotificationCreate
from src.db.postgres import get_session

router = APIRouter()


@router.get("/notifications/{notification_id}", response_model=NotificationResponse)
async def get_notification(notification_id: int, db: AsyncSession = Depends(get_session)):
    notification = await notification.get_notification(db=db, notification_id=notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@router.post("/notifications/", response_model=NotificationResponse)
async def create_notification(notification: NotificationCreate, db: AsyncSession = Depends(get_session)):
    return await notification.create_notification(db=db, user_id=notification.user_id, message=notification.message)

@router.get("/notifications/", response_model=list[NotificationResponse])
async def get_all_notifications(db: AsyncSession = Depends(get_session)):
    return await notification.get_all_notifications(db=db)