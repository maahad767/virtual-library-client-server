from typing import Any
from ninja import ModelSchema, Schema
from ninja.errors import ValidationError


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
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    password1: str
    password2: str

    def validate_password(self) -> Any:
        if self.password1 != self.password2:
            raise ValidationError("Passwords do not match.")
