from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .db import SessionLocal
from .settings import settings
from .utils import decode_token

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(authorization: str = Header(None)):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    token = authorization.split(" ",1)[1]
    try:
        payload = decode_token(token, settings.JWT_SECRET)
        return payload.get("sub")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
