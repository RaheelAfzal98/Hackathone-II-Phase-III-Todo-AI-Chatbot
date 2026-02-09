from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt  # Use pyjwt instead of jose
from datetime import datetime, timedelta
from typing import Optional
from ..config.settings import settings


# Initialize security scheme
security = HTTPBearer()

# Get secret key from settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def verify_token(token: str):
    """Verify JWT token and return decoded payload."""
    try:
        # Decode the token using the secret key
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract user information from payload
        user_id = payload.get("sub")
        exp = payload.get("exp")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Could not validate credentials: Missing user ID"
            )

        if exp is None:
            raise HTTPException(
                status_code=401,
                detail="Could not validate credentials: Missing expiration"
            )

        # Check if token is expired
        if datetime.fromtimestamp(exp) < datetime.now():
            raise HTTPException(
                status_code=401,
                detail="Token has expired"
            )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired"
        )
    except jwt.DecodeError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials"
        )
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=f"Authentication error: {str(e)}"
        )


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a new access token."""
    to_encode = data.copy()

    # Set expiration
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)

    to_encode.update({"exp": expire.timestamp()})

    # Encode the token
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Dependency to get the current user from the JWT token."""
    token = credentials.credentials
    user = verify_token(token)
    return user