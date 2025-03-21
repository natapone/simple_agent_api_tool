from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.services.datetime_service import DateTimeService
from app.api.endpoints import router as api_router
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    description="""
    A simple API for datetime operations with timezone support.
    
    ## Features
    - Get current datetime in ISO format
    - Get current week number
    - Timezone support for all operations
    
    ## Usage
    ```bash
    # Get current datetime
    curl "http://localhost:8005/api/v1/datetime?timezone=UTC"
    
    # Get week number
    curl "http://localhost:8005/api/v1/week-number?timezone=UTC"
    ```
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests for debugging purposes."""
    logger.info(f"Received request: {request.method} {request.url}")
    logger.info(f"Headers: {request.headers}")
    try:
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    """Root endpoint returning API information."""
    logger.info("Root endpoint called")
    return {
        "name": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "datetime": "/api/v1/datetime",
            "week_number": "/api/v1/week-number"
        }
    } 