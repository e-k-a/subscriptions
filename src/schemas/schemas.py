from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class AccountResponse(BaseModel):
    id: int
    balance: float
    last_updated: datetime

    class Config:
        from_attributes = True

class PaymentCreate(BaseModel):
    user_id: int
    subscription_id: Optional[int]
    amount: float

    class Config:
        from_attributes = True

class PaymentResponse(BaseModel):
    id: int
    user_id: int
    subscription_id: Optional[int]
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True


class PaymentMethodCreate(BaseModel):
    user_id: int
    card_number: str
    card_holder: str
    expiry_date: str
    cvv: str
    balance: float
    is_default: Optional[bool] = False

    class Config:
        from_attributes = True

class PaymentMethodResponse(BaseModel):
    id: int
    user_id: int
    card_number: str
    card_holder: str
    expiry_date: str
    cvv: str
    is_default: bool

    class Config:
        from_attributes = True

class NotificationCreate(BaseModel):
    user_id: int
    message: str

    class Config:
        from_attributes = True

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    message: str
    created_at: datetime

    class Config:
        from_attributes = True

class SubscriptionBase(BaseModel):
    name: str
    price: float
    auto_renew: bool

class SubscriptionCreate(SubscriptionBase):
    user_id: int
    name: str
    price: float
    auto_renew: bool
    duration_days: int

class SubscriptionResponse(SubscriptionBase):
    id: int
    expires_at: datetime
    class Config:
        from_attributes = True

