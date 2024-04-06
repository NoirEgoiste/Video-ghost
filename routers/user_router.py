from fastapi import APIRouter

from schemas.user_schemas import User, CreateUser

router = APIRouter(prefix="Users", tags=["Users"])


@router.get("/users")
async def get_user():
    hello = "Hello world"
    return hello


@router.post("/", response_model=User)
async def create_user(schema: User):
    pass
