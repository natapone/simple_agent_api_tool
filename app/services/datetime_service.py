from datetime import datetime
import pytz
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class DateTimeService:
    """Service for handling datetime operations."""
    
    def __init__(self):
        """Initialize the DateTimeService."""
        self.logger = logging.getLogger(__name__)
    
    def _validate_timezone(self, timezone: str) -> None:
        """
        Validate if the provided timezone is valid.
        
        Args:
            timezone (str): Timezone name to validate
            
        Raises:
            ValueError: If the timezone is invalid
        """
        try:
            pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            self.logger.error(f"Invalid timezone provided: {timezone}")
            raise ValueError(f"Invalid timezone: {timezone}")
    
    def get_current_datetime(self, timezone: Optional[str] = "UTC") -> str:
        """
        Get current datetime in ISO format for the specified timezone.
        
        Args:
            timezone (str, optional): Timezone name. Defaults to "UTC".
            
        Returns:
            str: Current datetime in ISO format
            
        Raises:
            ValueError: If the timezone is invalid
        """
        self.logger.info(f"Getting current datetime for timezone: {timezone}")
        self._validate_timezone(timezone)
        
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            iso_format = current_time.isoformat()
            self.logger.info(f"Successfully generated datetime: {iso_format}")
            return iso_format
        except Exception as e:
            self.logger.error(f"Error getting current datetime: {str(e)}")
            raise
    
    def get_week_number(self, timezone: Optional[str] = "UTC") -> int:
        """
        Get current week number for the specified timezone.
        
        Args:
            timezone (str, optional): Timezone name. Defaults to "UTC".
            
        Returns:
            int: Current week number
            
        Raises:
            ValueError: If the timezone is invalid
        """
        self.logger.info(f"Getting week number for timezone: {timezone}")
        self._validate_timezone(timezone)
        
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            week_number = current_time.isocalendar()[1]
            self.logger.info(f"Successfully generated week number: {week_number}")
            return week_number
        except Exception as e:
            self.logger.error(f"Error getting week number: {str(e)}")
            raise 