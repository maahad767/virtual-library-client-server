import jwt
from datetime import datetime, timedelta
from django.conf import settings


def create_access_token(user_id: int):
    payload = {
        "user_id": user_id,
        "type": "access",
        "exp": datetime.utcnow()
        + timedelta(minutes=30),  # Access token expires in 30 minutes
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def create_refresh_token(user_id: int):
    payload = {
        "user_id": user_id,
        "type": "refresh",
        "exp": datetime.utcnow() + timedelta(days=7),  # Refresh token expires in 7 days
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def decode_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    
    except jwt.ExpiredSignatureError:
        raise  # Handle expired token
    
    except jwt.DecodeError:
        raise 
    