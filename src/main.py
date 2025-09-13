from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from contextlib import asynccontextmanager

from routes import employees
from database import create_indexes, ensure_collection_validator
from auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

# --------------------------------
# Auth Router (for token endpoint)
# --------------------------------
router = APIRouter()

@router.post("/token", summary="User login to get JWT token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2-compatible login endpoint.
    Accepts username and password, returns JWT access token if valid.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]},  # Subject of the token
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --------------------------------
# Application Lifespan Events
# --------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Async startup/shutdown lifecycle:
    - Ensures MongoDB indexes and schema validation are in place.
    """
    await create_indexes()
    await ensure_collection_validator()
    yield
    # Optional: Cleanup logic here (e.g., closing DB connections)

# --------------------------------
# Initialize FastAPI App
# --------------------------------
app = FastAPI(lifespan=lifespan)

# --------------------------------
# CORS Middleware Configuration
# --------------------------------
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------
# Route Registrations
# --------------------------------
app.include_router(router, tags=["Auth"])  # /token route
app.include_router(employees.router, prefix="/employees", tags=["Employees"])

# --------------------------------
# Server Startup
# --------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
