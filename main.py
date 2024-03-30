from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import FileResponse

from Routers.user_router import router as user_router
from Routers.video_router import router as video_router

app = FastAPI(
    debug=True,
    title="Video Ghost",
    description="Video hosting site",
    version="0.1.0",
)

app.include_router(user_router)
app.include_router(video_router)
