# DateTime API Component Design

## Overview
The DateTime API component is a custom component for Langflow that provides datetime-related functionality through a FastAPI backend. It allows users to get current datetime and week numbers with timezone support.

## Component Structure

### Class Definition
```python
class DateTimeAPICore(Component):
    display_name = "DateTime API"
    description = "Get current datetime and week number with timezone support."
    icon = "datetime"
    name = "DateTimeAPI"
```

### Configuration
- **API URL**: Hardcoded to `http://host.docker.internal:8005` to support Docker container access
- **Default Timezone**: UTC

### Inputs
1. **Timezone** (Optional)
   - Type: Text Input
   - Default: "UTC"
   - Description: Timezone name (e.g., UTC, America/New_York)
   - If left empty, defaults to UTC

### Outputs
1. **DateTime**
   - Type: Data
   - Method: `get_datetime`
   - Returns: Current datetime in ISO format

2. **Week Number**
   - Type: Message
   - Method: `get_week_number`
   - Returns: Current week number

3. **DataFrame**
   - Type: DataFrame
   - Method: `as_dataframe`
   - Returns: Combined data including datetime, week number, and timezone

## Implementation Details

### Request Handling
- Uses `httpx` for HTTP requests
- 5-second timeout for all requests
- Automatic UTC fallback for empty timezone values
- Comprehensive error handling for:
  - Connection errors
  - Timeout errors
  - HTTP errors
  - General exceptions

### Error Handling
- Connection errors: Returns descriptive message about API connectivity
- Timeout errors: Indicates server responsiveness issues
- HTTP errors: Returns specific error messages from the API
- Empty timezone: Automatically uses UTC

## Usage Example
```python
# The component will automatically connect to the API
# and handle timezone conversion
result = component.get_datetime()  # Returns current datetime
week = component.get_week_number()  # Returns current week number
data = component.as_dataframe()  # Returns all data in DataFrame format
```

## Dependencies
- `httpx`: For making HTTP requests
- FastAPI backend running on port 8005
- Docker container support (using host.docker.internal)

## Notes
- The component is designed to work within a Docker container environment
- All API requests are made to the host machine using host.docker.internal
- Empty timezone values are automatically converted to UTC
- Error messages are user-friendly and descriptive 