from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.user import router as user_router

app = FastAPI()

app.include_router(user_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to Events Calendar API"}


@app.get("/health")
async def health():
    return {"status": "ok"}
