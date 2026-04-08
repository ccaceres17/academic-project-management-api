from fastapi import Request, HTTPException
from app.utils.jwt_handler import verify_token


def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(401, "Token missing")

    try:
        token = auth_header.split(" ")[1]
    except:
        raise HTTPException(401, "Invalid token format")

    payload = verify_token(token)

    if not payload:
        raise HTTPException(401, "Invalid or expired token")

    return payload