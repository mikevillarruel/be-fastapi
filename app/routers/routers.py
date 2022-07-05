from fastapi import APIRouter, Depends

from app.di import use_cases
from app.models import User
from app.use_cases import UserUseCases

user_router = APIRouter()


@user_router.get("/{id}", response_model=User)
def get_user(id: int, use_case: UserUseCases = Depends(use_cases.get_user_use_case)) -> User:
    return use_case.get_user(id)
