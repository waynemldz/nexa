from fastapi import FastAPI
from app.routes.message_routes import router
from app.routes.admin_routes import router as admin_router

app = FastAPI()

app.include_router(router)
app.include_router(admin_router)