# Development Setup Guide

## Prerequisites

- Python 3.11
- Git
- Virtual environment (recommended)

## Development Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simple_agent_api_tool.git
cd simple_agent_api_tool
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

4. Set up pre-commit hooks:
```bash
pre-commit install
```

5. Create a local `.env` file:
```bash
cp .env.example .env
# Edit .env with your settings
```

## Project Structure

```
simple_agent_api_tool/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py  # API route handlers
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py     # Configuration management
│   │   └── security.py   # API key validation
│   └── services/
│       ├── __init__.py
│       └── datetime_service.py  # Business logic
├── tests/
│   └── test_api.py
├── docs/
│   ├── api/
│   │   └── endpoints.md
│   └── development/
│       ├── setup.md
│       └── design.md
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Git Configuration

### .gitignore

The project includes a `.gitignore` file that excludes:
- Python virtual environment (`venv/`)
- Python cache files (`__pycache__/`, `*.pyc`, `*.pyo`, `*.pyd`)
- Distribution files (`dist/`, `build/`, `*.egg-info/`)
- Environment files (`.env`)
- IDE specific files (`.vscode/`, `.idea/`, `*.swp`, `*.swo`)
- Test coverage reports (`.coverage`, `htmlcov/`)
- Log files (`*.log`)

## Development Tools

### Code Formatting and Linting

1. **Black** - Code formatting:
```bash
black app tests
```

2. **isort** - Import sorting:
```bash
isort app tests
```

3. **Flake8** - Code linting:
```bash
flake8 app tests
```

4. **Mypy** - Type checking:
```bash
mypy app tests
```

### Testing

1. Run all tests:
```bash
pytest
```

2. Run tests with coverage:
```bash
pytest --cov=app tests/
```

3. Run specific test file:
```bash
pytest tests/test_api.py
```

### Development Server

Start the development server with auto-reload:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8003 --reload
```

## API Documentation

When running the server, access the API documentation at:
- Swagger UI: `http://localhost:8003/docs`
- ReDoc: `http://localhost:8003/redoc`

## Environment Variables

Required environment variables in `.env`:
```
API_KEY=your-api-key-here
API_RATE_LIMIT_PER_MINUTE=100
API_RATE_LIMIT_PER_HOUR=1000
HOST=0.0.0.0
PORT=8003
DEBUG=False
LOG_LEVEL=INFO
```

## Troubleshooting

### Common Issues

1. Import errors:
   - Verify Python version: `python --version`
   - Check virtual environment is activated
   - Verify all dependencies are installed: `pip list`

2. Test failures:
   - Check test environment setup
   - Verify test dependencies are installed
   - Check if `.env` file is properly configured

3. Server startup issues:
   - Check port availability
   - Verify environment variables
   - Check Python version compatibility

### Getting Help

1. Check the error logs
2. Review the documentation
3. Search for similar issues in the repository
4. Create a new issue with:
   - Description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details 