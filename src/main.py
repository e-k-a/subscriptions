

import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles

from src.api.v1 import users, account, payment_method, payments, notification, subscription
from src.core.settings import settings

app = FastAPI(
    docs_url="/api/docs",
)
# app.mount("/static", StaticFiles(directory="static"), name="static")


# app.include_router(payment.router, prefix="/billing_api/v1", tags=["payment"])

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(subscription.router, prefix="/api/v1/subscription", tags=["Subscriptions"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["Payments"])
app.include_router(payment_method.router, prefix="/api/v1/payment_method", tags=["Payment method"])
app.include_router(notification.router, prefix="/api/v1/notification", tags=["Notifications"])


if __name__ == '__main__':
    reload = settings.debug
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level=logging.DEBUG,
        reload=reload,
    )
