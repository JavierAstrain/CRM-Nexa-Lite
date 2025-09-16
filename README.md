# Nexa CRM (Lite) — Monorepo
**Stack**
- Frontend: Next.js (React + TypeScript), Tailwind CSS, shadcn/ui, Recharts, dnd-kit.
- Backend: FastAPI (Python), SQLAlchemy, Alembic-like migrations (simple), JWT Auth.
- DB: PostgreSQL (Render) o SQLite local (dev). Redis opcional.
- IA: OpenAI API (resúmenes, score de oportunidades, borradores de email).

## Deploy rápido (Render)
1. **PostgreSQL**: crea un servicio Postgres en Render y copia su `DATABASE_URL`.
2. **Backend** (Web Service - Python):
   - Build: `pip install -r backend/requirements.txt`
   - Start: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
   - Env:
     - `DATABASE_URL` (postgres://...)
     - `OPENAI_API_KEY`
     - `JWT_SECRET` (alguna cadena segura)
     - `FRONTEND_ORIGIN` (por ej: https://nexa-frontend.onrender.com)
3. **Frontend** (Web Service - Node):
   - Build: `cd frontend && npm install && npm run build`
   - Start: `npm run start`
   - Env:
     - `NEXT_PUBLIC_API_BASE` (URL del backend, ej. https://nexa-backend.onrender.com)

## Desarrollo local
```bash
# Backend
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
export DATABASE_URL="sqlite:///./nexa.db"
export OPENAI_API_KEY="sk-..."
export JWT_SECRET="devsecret"
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## IA (OpenAI)
Endpoints:
- `POST /ai/sales-insights` -> insights desde deals/actividades.
- `POST /ai/draft-email` -> borrador de correo.
- `POST /ai/score-deal` -> prob. ganar (heurístico+IA).

## i18n
Arquitectura de archivos en `frontend/locales/{es,en,pt}.json`.

## Favicon y logos
Coloca `Isotipo_Nexa.png` como favicon y en el header. `Nexa_logo.png` en login.
