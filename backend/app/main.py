from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine, init_db
from .routers import auth, companies, contacts, pipelines, deals, tasks, interactions, dashboard, ai
from .settings import settings

app = FastAPI(title="Nexa CRM (Lite)", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN, "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(companies.router, prefix="/companies", tags=["companies"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
app.include_router(pipelines.router, prefix="/pipelines", tags=["pipelines"])
app.include_router(deals.router, prefix="/deals", tags=["deals"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(interactions.router, prefix="/interactions", tags=["interactions"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])

@app.get("/health")
def health():
    return {"status": "ok"}
