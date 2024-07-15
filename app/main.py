from app.api.v1.routers import maintenances, remittances, reports
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix=settings.API_V1_STR)

app.include_router(
    maintenances.router,
    prefix="/maintenances",
    tags=["maintenances"])
app.include_router(
    remittances.router,
    prefix="/remittances",
    tags=["remittances"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])
