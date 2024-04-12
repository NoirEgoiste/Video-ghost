from fastapi import APIRouter

router = APIRouter(prefix="/Videos", tags=["Videos"])


@router.get("/")
async def get_videos():
    pass
