from fastapi import FastAPI

from routers.user_router import router as user_router
from routers.video_router import router as video_router

app = FastAPI(
    debug=True,
    title="Video Ghost",
    description="Video hosting site",
    version="0.1.0",
)

app.include_router(user_router)
app.include_router(video_router)
