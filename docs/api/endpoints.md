# API Documentation

## Overview

This document provides detailed information about the API endpoints available in this service.

## Authentication

All endpoints require API key authentication using the `X-API-Key` header.

Example:
```bash
curl -H "X-API-Key: your-api-key" http://localhost:8003/api/v1/datetime
```

## Endpoints

### Current DateTime

Get the current date and time with timezone support.

**Endpoint:** `GET /api/v1/datetime`

**Headers:**
- `X-API-Key`: Your API key

**Query Parameters:**
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| timezone | string | No | "UTC" | Timezone identifier (e.g., 'UTC', 'America/New_York') |

**Response:**
```json
{
    "datetime": "2024-03-20T10:30:00-04:00"
}
```

**Error Responses:**
- 400 Bad Request: Invalid timezone format
- 401 Unauthorized: Missing or invalid API key
- 404 Not Found: Timezone not found

### Week Number

Get the current week number with timezone support.

**Endpoint:** `GET /api/v1/week-number`

**Headers:**
- `X-API-Key`: Your API key

**Query Parameters:**
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| timezone | string | No | "UTC" | Timezone identifier (e.g., 'UTC', 'America/New_York') |

**Response:**
```json
{
    "week_number": 12
}
```

**Error Responses:**
- 400 Bad Request: Invalid timezone format
- 401 Unauthorized: Missing or invalid API key
- 404 Not Found: Timezone not found

## Timezone Support

The API supports all timezones available in the IANA Time Zone Database. Common timezone identifiers include:

- UTC
- America/New_York
- America/Los_Angeles
- Europe/London
- Asia/Tokyo
- Australia/Sydney

For a complete list of supported timezones, refer to the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

## Rate Limiting

The API implements rate limiting to prevent abuse. Limits are:
- 100 requests per minute per API key
- 1000 requests per hour per API key

When rate limits are exceeded, the API will return a 429 Too Many Requests response.

## Error Handling

All endpoints follow a consistent error response format:

```json
{
    "error": {
        "code": "ERROR_CODE",
        "message": "Human readable error message",
        "details": {} // Optional additional error details
    }
}
```

Common error codes:
- `INVALID_API_KEY`: API key is missing or invalid
- `INVALID_TIMEZONE`: Timezone format is invalid
- `TIMEZONE_NOT_FOUND`: Requested timezone does not exist
- `RATE_LIMIT_EXCEEDED`: Rate limit exceeded 