# DateTime Tools for Langflow

A simple custom component for Langflow that provides datetime-related tools with timezone support.

## Features

- Get current date and time with timezone support
- Get current week number with timezone support
- Simple error handling for invalid timezones

## Installation

1. Copy the contents of `langflow_component.py`
2. Open Langflow
3. Click "+ Custom Component"
4. Paste the code into the editor
5. Click "Check & Save"

## Usage

### Get Current DateTime

```python
datetime_tools = DateTimeTools()
current_time = datetime_tools.get_current_datetime("America/New_York")
# Returns: "2024-03-20T10:30:00-04:00"
```

### Get Week Number

```python
datetime_tools = DateTimeTools()
week_num = datetime_tools.get_week_number("America/New_York")
# Returns: 12
```

## Timezone Support

The component supports all timezones available in the IANA Time Zone Database. Common timezone identifiers include:

- UTC
- America/New_York
- America/Los_Angeles
- Europe/London
- Asia/Tokyo
- Australia/Sydney

For a complete list of supported timezones, refer to the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

## Error Handling

- Invalid timezones will return an error message
- Week number will return -1 for invalid timezones or errors

## Dependencies

The component requires the following Python packages:
- pytz
- datetime (built-in)

Make sure these are installed in your Langflow environment.
