from fastapi import APIRouter, HTTPException
from typing import Optional
import logging
from app.services.datetime_service import DateTimeService
from app.core.config import settings

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/datetime", 
    response_model=dict,
    summary="Get current datetime",
    description="""
    Get the current datetime in ISO format for the specified timezone.
    
    Args:
        timezone (str, optional): Timezone name (e.g., UTC, America/New_York). Defaults to UTC.
    
    Returns:
        dict: A dictionary containing the current datetime in ISO format.
    
    Raises:
        HTTPException: If the timezone is invalid or there's an error processing the request.
    """
)
async def get_current_datetime(timezone: Optional[str] = settings.TIMEZONE):
    """Get current datetime in ISO format."""
    logger.info(f"Getting current datetime for timezone: {timezone}")
    try:
        service = DateTimeService()
        result = service.get_current_datetime(timezone)
        logger.info(f"Successfully retrieved datetime: {result}")
        return {"datetime": result}
    except ValueError as e:
        logger.error(f"Invalid timezone: {timezone}")
        raise HTTPException(
            status_code=400,
            detail=f"Invalid timezone: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error getting datetime: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/week-number",
    response_model=dict,
    summary="Get current week number",
    description="""
    Get the current week number for the specified timezone.
    
    Args:
        timezone (str, optional): Timezone name (e.g., UTC, America/New_York). Defaults to UTC.
    
    Returns:
        dict: A dictionary containing the current week number.
    
    Raises:
        HTTPException: If the timezone is invalid or there's an error processing the request.
    """
)
async def get_week_number(timezone: Optional[str] = settings.TIMEZONE):
    """Get current week number."""
    logger.info(f"Getting week number for timezone: {timezone}")
    try:
        service = DateTimeService()
        result = service.get_week_number(timezone)
        logger.info(f"Successfully retrieved week number: {result}")
        return {"week_number": result}
    except ValueError as e:
        logger.error(f"Invalid timezone: {timezone}")
        raise HTTPException(
            status_code=400,
            detail=f"Invalid timezone: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error getting week number: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 