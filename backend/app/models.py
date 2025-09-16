from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric, Text, Boolean, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from .db import Base

def ts():
    return datetime.utcnow()

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String, ForeignKey("accounts.id"))
    email: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    locale: Mapped[str] = mapped_column(String, default="es")
    password_hash: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String, default="member")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=ts)

class Company(Base):
    __tablename__ = "companies"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String, index=True)
    industry: Mapped[str] = mapped_column(String, nullable=True)
    website: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    country: Mapped[str] = mapped_column(String, nullable=True)
    city: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    owner_user_id: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=ts)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=ts)

class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String)
    company_id: Mapped[str] = mapped_column(String, ForeignKey("companies.id"), nullable=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, index=True, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    job_title: Mapped[str] = mapped_column(String, nullable=True)
    linkedin: Mapped[str] = mapped_column(String, nullable=True)
    tags: Mapped[str] = mapped_column(String, nullable=True)  # CSV simple
    owner_user_id: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=ts)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=ts)

class Pipeline(Base):
    __tablename__ = "pipelines"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False)

class Stage(Base):
    __tablename__ = "stages"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String)
    pipeline_id: Mapped[str] = mapped_column(String, ForeignKey("pipelines.id"))
    name: Mapped[str] = mapped_column(String)
    order: Mapped[int] = mapped_column(Integer)
    probability: Mapped[float] = mapped_column(Numeric, default=0.0)
    color: Mapped[str] = mapped_column(String, nullable=True)

class Deal(Base):
    __tablename__ = "deals"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String)
    pipeline_id: Mapped[str] = mapped_column(String, ForeignKey("pipelines.id"))
    stage_id: Mapped[str] = mapped_column(String, ForeignKey("stages.id"))
    company_id: Mapped[str] = mapped_column(String, ForeignKey("companies.id"), nullable=True)
    primary_contact_id: Mapped[str] = mapped_column(String, ForeignKey("contacts.id"), nullable=True)
    title: Mapped[str] = mapped_column(String)
    amount: Mapped[float] = mapped_column(Numeric, default=0.0)
    currency: Mapped[str] = mapped_column(String, default="CLP")
    expected_close_date: Mapped[datetime] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(String, default="open")
    source: Mapped[str] = mapped_column(String, nullable=True)
    owner_user_id: Mapped[str] = mapped_column(String, nullable=True)
    tags: Mapped[str] = mapped_column(String, nullable=True)
    custom_fields: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=ts)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=ts)

class Interaction(Base):
    __tablename__ = "interactions"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String)
    contact_id: Mapped[str] = mapped_column(String, ForeignKey("contacts.id"), nullable=True)
    company_id: Mapped[str] = mapped_column(String, ForeignKey("companies.id"), nullable=True)
    type: Mapped[str] = mapped_column(String)
    subject: Mapped[str] = mapped_column(String, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    direction: Mapped[str] = mapped_column(String, nullable=True)
    happened_at: Mapped[datetime] = mapped_column(DateTime, default=ts)
    created_by: Mapped[str] = mapped_column(String, nullable=True)

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    account_id: Mapped[str] = mapped_column(String)
    related_type: Mapped[str] = mapped_column(String, nullable=True)
    related_id: Mapped[str] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String, nullable=True)
    due_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    reminder_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    priority: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, default="open")
    assignee_user_id: Mapped[str] = mapped_column(String, nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
