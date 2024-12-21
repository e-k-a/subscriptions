import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles

from src.api.v1 import notifications, payments, subscriptions, users, payment_methods
from src.core.settings import settings

app = FastAPI(
    docs_url="/api/docs",
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(subscriptions.router, prefix="/subscription", tags=["Subscriptions"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(
    payment_methods.router, prefix="/payment_method", tags=["Payment method"]
)
app.include_router(notifications.router, prefix="/notification", tags=["Notifications"])


if __name__ == "__main__":
    reload = settings.debug
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level=logging.DEBUG,
        reload=reload,
    )
