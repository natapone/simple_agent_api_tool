# API Documentation

## Components Overview

This document provides detailed information about the datetime components available in this package.

## Current DateTime Component

### Overview
The Current DateTime component provides current date and time information with timezone support. It uses Python's `datetime` module and `pytz` for timezone handling.

### Component Details
- **Name**: `CurrentDateTime`
- **Category**: `datetime`
- **Display Name**: "Current DateTime"
- **Description**: Get current date and time with timezone support

### Inputs
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| timezone | string | No | "UTC" | Timezone identifier (e.g., 'UTC', 'America/New_York') |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| datetime | string | Current date and time in ISO format with timezone |

### Example Usage
```python
# In Langflow
component = CurrentDateTimeComponent()
result = component.get_datetime(timezone="America/New_York")
# Output: "2024-03-20T10:30:00-04:00"
```

## Week Number Component

### Overview
The Week Number component provides the current week number with timezone support. It uses Python's `datetime` module and `pytz` for timezone handling.

### Component Details
- **Name**: `WeekNumber`
- **Category**: `datetime`
- **Display Name**: "Week Number"
- **Description**: Get current week number with timezone support

### Inputs
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| timezone | string | No | "UTC" | Timezone identifier (e.g., 'UTC', 'America/New_York') |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| week_number | integer | Current week number (1-53) |

### Example Usage
```python
# In Langflow
component = WeekNumberComponent()
result = component.get_week_number(timezone="America/New_York")
# Output: 12
```

## Error Handling

Both components handle the following error cases:

1. Invalid Timezone
   - Error Message: "Invalid timezone: {timezone}"
   - Status Code: 400

2. Timezone Not Found
   - Error Message: "Timezone {timezone} not found"
   - Status Code: 404

## Timezone Support

The components support all timezones available in the IANA Time Zone Database. Common timezone identifiers include:

- UTC
- America/New_York
- America/Los_Angeles
- Europe/London
- Asia/Tokyo
- Australia/Sydney

For a complete list of supported timezones, refer to the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). 