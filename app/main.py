from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from app.core.config import settings
from app.core.database import engine
from app import models

from app.api.routes import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.TITLE, version="1.0")

app.add_middleware(
    # HTTPSRedirectMiddleware,
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
