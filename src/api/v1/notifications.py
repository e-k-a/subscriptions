from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud import notification
from src.schemas.schemas import NotificationResponse, NotificationCreate
from src.db.postgres import get_session

router = APIRouter()


@router.get("/{notification_id}", response_model=NotificationResponse)
async def get_notification(
    notification_id: int, db: AsyncSession = Depends(get_session)
):
    notification_res = await notification.get_notification(
        db=db, notification_id=notification_id
    )
    if not notification_res:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification_res


@router.post("/", response_model=NotificationResponse)
async def create_notification(
    notification_data: NotificationCreate, db: AsyncSession = Depends(get_session)
):
    return await notification.create_notification(
        db=db, user_id=notification_data.user_id, message=notification_data.message
    )


@router.get("/", response_model=list[NotificationResponse])
async def get_all_notifications(db: AsyncSession = Depends(get_session)):
    return await notification.get_all_notifications(db=db)
