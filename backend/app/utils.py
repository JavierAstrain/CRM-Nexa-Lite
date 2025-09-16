import uuid, hashlib, os, jwt, datetime
from passlib.hash import bcrypt

def new_id():
    return uuid.uuid4().hex

def hash_password(pw:str) -> str:
    return bcrypt.hash(pw)

def verify_password(pw:str, pw_hash:str) -> bool:
    return bcrypt.verify(pw, pw_hash)

def create_token(user_id:str, secret:str):
    payload = {"sub": user_id, "exp": datetime.datetime.utcnow()+datetime.timedelta(days=7)}
    return jwt.encode(payload, secret, algorithm="HS256")

def decode_token(token:str, secret:str):
    return jwt.decode(token, secret, algorithms=["HS256"])
