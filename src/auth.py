from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# -----------------------------
# Configuration Constants
# -----------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")  # Default for dev; change in prod!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expiration time

# -----------------------------
# Password Hashing Context
# -----------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 Scheme for FastAPI dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# -----------------------------
# Dummy User Database (for demo purposes)
# -----------------------------
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("adminpass")  # Hashed using passlib
    }
}

# -----------------------------
# Utility Functions
# -----------------------------

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a hashed one using passlib.
    """
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    """
    Authenticates a user from the fake database.
    Returns user dict if valid, otherwise False.
    """
    user = fake_users_db.get(username)
    if not user or not verify_password(password, user["hashed_password"]):
        return False
    return {"username": username}

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Creates a JWT access token with optional expiration.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "sub": data.get("username")})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# -----------------------------
# Dependency: Get Current User
# -----------------------------

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Decodes and verifies the JWT token to get the current user.
    Raises HTTP 401 if token is invalid or user not found.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = fake_users_db.get(username)
    if user is None:
        raise credentials_exception

    return {"username": username}
