from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from src.db.postgres import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    subscriptions = relationship("Subscription", back_populates="user", lazy='selectin')
    payment_methods = relationship("PaymentMethod", back_populates="user", lazy='selectin')
    # account = relationship("Account", uselist=False, back_populates="user", lazy='selectin')

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    price = Column(Float)
    is_active = Column(Boolean, default=True)
    expires_at = Column(DateTime)
    auto_renew = Column(Boolean, default=False)
    user = relationship("User", back_populates="subscriptions")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=True)
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.now)

class PaymentMethod(Base):
    __tablename__ = "payment_methods"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    card_number = Column(String, unique=True)
    card_holder = Column(String)
    expiry_date = Column(String)
    balance = Column(Float, default=0.0)

    cvv = Column(String)
    is_default = Column(Boolean, default=False)
    user = relationship("User", back_populates="payment_methods")

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

