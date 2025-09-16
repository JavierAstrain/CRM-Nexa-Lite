from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..deps import get_db, get_current_user
from .. import models
from ..utils import new_id

router = APIRouter()

@router.get("/")
def list_deals(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    return db.query(models.Deal).all()

@router.post("/")
def create_deals(payload: dict, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    obj = models.Deal(**{{"id": new_id(), **payload}})
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@router.get("/{obj_id}")
def get_deals(obj_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    obj = db.query(models.Deal).filter(models.Deal.id==obj_id).first()
    if not obj: raise HTTPException(404)
    return obj

@router.put("/{obj_id}")
def update_deals(obj_id: str, payload: dict, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    obj = db.query(models.Deal).filter(models.Deal.id==obj_id).first()
    if not obj: raise HTTPException(404)
    for k,v in payload.items(): setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    return obj

@router.delete("/{obj_id}")
def delete_deals(obj_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    obj = db.query(models.Deal).filter(models.Deal.id==obj_id).first()
    if not obj: raise HTTPException(404)
    db.delete(obj); db.commit(); return {{"ok": True}}
