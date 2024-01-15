from typing import Any
from ninja import ModelSchema, Schema, Field
from ninja.errors import ValidationError
from pydantic import EmailStr

import re

from account.models import User


class AuthIn(Schema):
    username: str
    password: str


class AuthRefreshIn(Schema):
    refresh: str


class AuthOut(Schema):
    access_token: str
    refresh_token: str


class RegisterIn(ModelSchema):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=150)

    class Config:
        model = User
        model_fields = ["username", "first_name", "last_name", "email"]

    password1: str
    password2: str

    def validate_username(self) -> Any:
        if not re.match(r"^[\w.@+-]+\Z", self.username):
            raise ValidationError(
                "Enter a valid username. This value may contain only letters, "
                "numbers, and @/./+/-/_ characters."
            )

    def validate_password(self) -> Any:
        if self.password1 != self.password2:
            raise ValidationError("Passwords do not match.")


class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = ["id", "username", "first_name", "last_name", "email"]
