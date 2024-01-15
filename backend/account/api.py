from django.contrib.auth import authenticate
from ninja import Router
from ninja.errors import HttpError

from account.models import User
from account.schema import AuthIn, AuthRefreshIn, AuthOut, RegisterIn
from account.utils import create_access_token, create_refresh_token, decode_token
from common.schema import GenericResponse

router = Router()


@router.post("token/", response=AuthOut, auth=None)
def get_token(request, auth_in: AuthIn):
    user = authenticate(username=auth_in.username, password=auth_in.password)
    if user:
        access_token = create_access_token(user_id=user.id)
        refresh_token = create_refresh_token(user_id=user.id)
        return {"access_token": access_token, "refresh_token": refresh_token}
    raise HttpError(401, "Invalid username or password")


@router.post("refresh/", auth=None)
def refresh_token(request, refresh_in: AuthRefreshIn):
    payload = decode_token(refresh_in.refresh)
    if payload and payload.get("type") == "refresh":
        user = User.objects.filter(id=payload["user_id"]).first()
        if user:
            new_access_token = create_access_token(user_id=user.id)
            return {
                "access_token": new_access_token,
                "refresh_token": refresh_in.refresh,
            }
    return HttpError(401, "Invalid refresh token")


@router.post("/register/", response=GenericResponse, auth=None)
def register_user(request, user_in: RegisterIn):
    user_in.validate_password()

    if User.objects.filter(username=user_in.username).exists():
        raise HttpError(400, "Username already taken")

    if User.objects.filter(email=user_in.email).exists():
        raise HttpError(400, "Email already taken")

    User.objects.create_user(username=user_in.username, email=user_in.email, password=user_in.password1, first_name=user_in.first_name, last_name=user_in.last_name)
    return {"message": "Registration successful"}
