# Design Document

## Overview

This project follows a two-phase approach:
1. Phase 1: Develop a FastAPI server with datetime tools endpoints
2. Phase 2: Create Python code snippets for Langflow to call these endpoints

## Phase 1: FastAPI Server

### System Requirements

#### Runtime Requirements
- Python 3.11
- FastAPI 0.109.2 or higher
- Uvicorn 0.27.1 or higher
- Pydantic 2.6.1 or higher
- PyTZ 2024.1 or higher
- Python-dateutil 2.8.2 or higher
- Python-dotenv 1.0.1 or higher

#### Development Requirements
- pytest 8.0.0 or higher
- pytest-cov 4.1.0 or higher
- black 24.2.0 or higher
- isort 5.13.2 or higher
- flake8 7.0.0 or higher
- mypy 1.8.0 or higher
- pre-commit 3.6.0 or higher

### API Server Architecture

```
[FastAPI Server] ---> [DateTime Services]
        |
        v
[Authentication & Rate Limiting]
```

### Component Design

1. **API Layer** (`app/api/`)
   - Handles HTTP requests and responses
   - Implements input validation
   - Routes requests to appropriate services
   - Manages error responses

2. **Core Services** (`app/core/`)
   - Configuration management
   - Security (API key validation)
   - Rate limiting
   - Logging

3. **Business Logic** (`app/services/`)
   - DateTime operations
   - Timezone handling
   - Week number calculations

### API Endpoints

1. **Current DateTime**
   - Path: `/api/v1/datetime`
   - Method: GET
   - Parameters: timezone (optional)
   - Response: ISO formatted datetime string

2. **Week Number**
   - Path: `/api/v1/week-number`
   - Method: GET
   - Parameters: timezone (optional)
   - Response: Integer week number

### Security Design

1. **API Key Authentication**
   - Required for all endpoints
   - Keys stored in environment variables
   - Header-based authentication (`X-API-Key`)

2. **Rate Limiting**
   - Per-key rate limiting
   - Configurable limits (minute/hour)
   - 429 responses for exceeded limits

## Phase 2: Langflow Integration

### Langflow Component Design

1. **Component Structure**
   ```python
   class DateTimeTools:
       """A collection of datetime tools for Langflow."""
       
       display_name = "DateTime Tools"
       description = "Get current date/time and week number with timezone support"
       documentation = "https://docs.langflow.org/components-custom-components"
       icon = "datetime"
       name = "DateTimeTools"
   ```

2. **API Integration Methods**
   ```python
   def get_current_datetime(self, timezone: Optional[str] = None) -> str:
       """Call API endpoint to get current datetime."""
       # Implementation will make HTTP call to API server

   def get_week_number(self, timezone: Optional[str] = None) -> int:
       """Call API endpoint to get week number."""
       # Implementation will make HTTP call to API server
   ```

### Error Handling

1. **API Server Errors**
   - Authentication errors (401)
   - Validation errors (400)
   - Rate limiting errors (429)
   - Server errors (500)

2. **Langflow Component Errors**
   - API connection errors
   - Invalid timezone errors
   - Rate limit exceeded errors

## Implementation Steps

### Phase 1: API Server Implementation
1. Set up FastAPI project structure
2. Implement core services (config, security)
3. Implement datetime services
4. Create API endpoints
5. Add error handling
6. Add rate limiting
7. Add logging
8. Test API endpoints
9. Document API usage

### Phase 2: Langflow Integration
1. Create Langflow component class
2. Implement API client methods
3. Add error handling
4. Add retry logic
5. Test component
6. Document component usage

## Configuration Management

### API Server Configuration
Environment variables (`.env`):
```
API_KEY=your-api-key-here
API_RATE_LIMIT_PER_MINUTE=100
API_RATE_LIMIT_PER_HOUR=1000
HOST=0.0.0.0
PORT=8003
DEBUG=False
LOG_LEVEL=INFO
```

### Langflow Component Configuration
- API endpoint URL
- API key
- Timeout settings
- Retry settings

## Testing Strategy

### Phase 1: API Testing
1. **Unit Tests**
   - Service layer testing
   - Model validation testing
   - Authentication testing
   - Rate limit testing

2. **Integration Tests**
   - API endpoint testing
   - Error handling testing
   - Configuration testing

3. **Load Tests**
   - Rate limiting verification
   - Concurrent request handling

### Phase 2: Component Testing
1. **Unit Tests**
   - API client testing
   - Error handling testing
   - Retry logic testing

2. **Integration Tests**
   - End-to-end API calls
   - Error scenarios
   - Rate limit handling

## Deployment

### API Server Deployment
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8003 --workers 4
```

### Langflow Component Deployment
1. Copy component code to Langflow
2. Configure API endpoint and key
3. Test in Langflow environment

## Monitoring and Logging

### API Server
1. **Logging**
   - Request/response logging
   - Error logging
   - Performance metrics

2. **Metrics**
   - Request count
   - Response times
   - Error rates
   - Rate limit hits

### Langflow Component
1. **Logging**
   - API call logging
   - Error logging
   - Performance metrics

## Future Enhancements

### API Server
1. **Short Term**
   - Additional datetime operations
   - Enhanced timezone support
   - More detailed error messages

2. **Long Term**
   - Database integration for API key management
   - OAuth2 authentication option
   - Caching layer
   - Metrics dashboard

### Langflow Component
1. **Short Term**
   - Additional API endpoint integrations
   - Enhanced error handling
   - Better retry logic

2. **Long Term**
   - Caching layer
   - Batch operations
   - Advanced error recovery 