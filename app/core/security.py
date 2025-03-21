from fastapi import HTTPException, Security, Header
from typing import Optional

from app.core.config import settings

async def get_api_key(
    x_api_key: Optional[str] = Header(None, alias="X-API-Key")
) -> str:
    """Validate API key from request header."""
    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="API key is missing"
        )
    
    if x_api_key != settings.API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    
    return x_api_key 