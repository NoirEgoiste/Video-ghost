from fastapi import FastAPI

from domain.confing import settings

from routers.user_router import router as user_router
from routers.video_router import router as video_router

app = FastAPI(
    app_name=settings.app_name,
    debug=settings.debug,
    title=settings.title,
    description=settings.description,
    version=settings.version,
)

app.include_router(user_router)
app.include_router(video_router)
