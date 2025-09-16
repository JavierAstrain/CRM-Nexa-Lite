from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from .. import models
from ..utils import new_id, hash_password, verify_password, create_token
from ..settings import settings

router = APIRouter()

@router.post("/register")
def register(email:str, password:str, name:str="User", account_name:str="Default"):
    db = SessionLocal()
    # naive: create account if not exist, user unique by email
    if db.query(models.User).filter(models.User.email==email).first():
        raise HTTPException(400, "Email already registered")
    acc = models.Account(id=new_id(), name=account_name)
    user = models.User(id=new_id(), account_id=acc.id, email=email, name=name, password_hash=hash_password(password))
    db.add_all([acc, user])
    db.commit()
    token = create_token(user.id, settings.JWT_SECRET)
    return {"token": token, "user_id": user.id, "account_id": acc.id}

@router.post("/login")
def login(email:str, password:str):
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.email==email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")
    token = create_token(user.id, settings.JWT_SECRET)
    return {"token": token, "user_id": user.id, "account_id": user.account_id}
