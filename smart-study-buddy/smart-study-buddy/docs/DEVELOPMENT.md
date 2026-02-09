# 🛠️ Development Guide - Smart Study Buddy

Complete guide for developers working on or extending Smart Study Buddy.

## 📁 Project Architecture

```
smart-study-buddy/
├── src/                    # Core application code
│   ├── __init__.py        # Package initialization
│   ├── ai_client.py       # AI provider abstraction layer
│   ├── prompts.py         # System prompts and templates
│   └── study_buddy.py     # Main application logic
│
├── notebooks/             # Jupyter/Colab notebooks
│   └── Smart_Study_Buddy.ipynb
│
├── examples/              # Example scripts
│   └── run_examples.py
│
├── tests/                 # Test suite
│   └── test_study_buddy.py
│
├── docs/                  # Documentation
│   ├── QUICKSTART.md
│   └── DEVELOPMENT.md (this file)
│
├── config/                # Configuration files
│
├── cli.py                 # Command-line interface
├── web_app.py            # Gradio web interface
├── api_server.py         # FastAPI REST API
├── demo.py               # Interactive demo
│
├── requirements.txt       # Python dependencies
├── .env                   # API keys (local, not in git)
├── .gitignore            # Git ignore rules
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
└── README.md             # Main documentation
```

## 🏗️ Core Components

### 1. AI Client (`src/ai_client.py`)

Abstraction layer supporting multiple AI providers:

```python
class AIClient:
    - __init__(provider, model)    # Initialize client
    - generate_explanation()        # Synchronous generation
    - stream_explanation()          # Streaming generation
```

**Supported Providers:**
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)

**Adding a new provider:**

```python
def _init_newprovider(self):
    """Initialize new provider client"""
    from newprovider import Client
    self.client = Client(api_key=os.getenv("NEWPROVIDER_KEY"))

def _generate_newprovider(self, system_prompt, user_prompt, **kwargs):
    """Generate using new provider"""
    response = self.client.complete(
        system=system_prompt,
        user=user_prompt,
        **kwargs
    )
    return response.text
```

### 2. Prompts (`src/prompts.py`)

System prompt engineering and template management:

```python
SYSTEM_PROMPT          # Core teaching instructions
AUDIENCE_LEVELS        # Predefined audience descriptions
create_user_prompt()   # Template function
```

**Modifying the system prompt:**

1. Edit `SYSTEM_PROMPT` constant
2. Test with various audiences
3. Update tests if behavior changes

### 3. Study Buddy (`src/study_buddy.py`)

Main application class:

```python
class SmartStudyBuddy:
    - explain()              # Generate explanation
    - explain_interactive()  # Interactive CLI mode
    - batch_explain()        # Multiple topics
    - get_history()          # Conversation tracking
```

## 🧪 Testing

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_study_buddy.py -v

# With coverage
pytest tests/ --cov=src --cov-report=html
```

### Writing Tests

```python
import pytest
from src.study_buddy import SmartStudyBuddy

def test_new_feature():
    """Test description"""
    buddy = SmartStudyBuddy()
    result = buddy.new_feature()
    assert result is not None
```

### Test Structure

- Unit tests: Test individual functions
- Integration tests: Test component interactions
- API tests: Test external API calls (mock in CI)

## 🎨 Adding New Features

### Example: Adding a "Summary" Feature

1. **Update Prompts** (`src/prompts.py`):

```python
def create_summary_prompt(content: str, length: str) -> str:
    return f"""
    Summarize this content:
    {content}
    
    Length: {length}
    """
```

2. **Add Method** (`src/study_buddy.py`):

```python
def summarize(self, content: str, length: str = "medium") -> str:
    prompt = create_summary_prompt(content, length)
    return self.client.generate_explanation(
        self.system_prompt,
        prompt
    )
```

3. **Add CLI Command** (`cli.py`):

```python
@app.command()
def summarize(
    text: str = typer.Argument(...),
    length: str = typer.Option("medium", "--length", "-l")
):
    buddy = SmartStudyBuddy()
    summary = buddy.summarize(text, length)
    console.print(Panel(summary))
```

4. **Add Tests** (`tests/test_study_buddy.py`):

```python
def test_summarize():
    buddy = SmartStudyBuddy()
    summary = buddy.summarize("Long text...", "short")
    assert len(summary) < len("Long text...")
```

5. **Update Documentation**:
   - Add to README.md
   - Add examples
   - Update API docs

## 🔌 API Development

### FastAPI Server (`api_server.py`)

**Adding New Endpoints:**

```python
@app.post("/new-endpoint")
async def new_endpoint(request: NewRequest):
    """Endpoint description"""
    try:
        buddy = get_buddy(request.provider)
        result = buddy.new_method(request.param)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**Testing API:**

```bash
# Start server
python api_server.py

# Test with curl
curl -X POST http://localhost:8000/explain \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "gravity",
    "audience": "child"
  }'

# Or use the interactive docs
open http://localhost:8000/docs
```

## 🎨 UI Development

### Gradio Web App (`web_app.py`)

**Adding New Components:**

```python
# Add input
new_input = gr.Textbox(
    label="New Input",
    placeholder="Enter..."
)

# Connect to function
new_btn.click(
    fn=new_function,
    inputs=[new_input],
    outputs=output_text
)
```

### CLI Development (`cli.py`)

**Adding Commands:**

```python
@app.command()
def new_command(
    arg: str = typer.Argument(..., help="Argument help"),
    option: str = typer.Option("default", "--opt", "-o")
):
    """Command description"""
    console.print(f"Processing {arg} with {option}")
```

## 📦 Packaging & Distribution

### Creating a Distribution

```bash
# Install build tools
pip install build twine

# Build
python -m build

# Upload to PyPI
twine upload dist/*
```

### Docker Deployment

```bash
# Build image
docker build -t smart-study-buddy .

# Run web interface
docker run -p 7860:7860 \
  -e OPENAI_API_KEY=your_key \
  smart-study-buddy

# Run API server
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_key \
  smart-study-buddy \
  python api_server.py

# Or use docker-compose
docker-compose up
```

## 🔄 CI/CD

### GitHub Actions Workflow (`.github/workflows/test.yml`):

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v
```

## 🎯 Best Practices

### Code Style

```bash
# Format code
black src/ tests/ cli.py web_app.py api_server.py

# Type checking
mypy src/

# Linting
pylint src/
```

### Commit Messages

```
feat: Add streaming support
fix: Resolve API timeout issue
docs: Update README with examples
test: Add tests for batch processing
refactor: Simplify prompt generation
```

### Environment Variables

```python
# Always use environment variables for secrets
api_key = os.getenv("API_KEY")

# Provide defaults for optional settings
max_tokens = int(os.getenv("MAX_TOKENS", "2000"))

# Use .env files for local development
from dotenv import load_dotenv
load_dotenv()
```

## 🐛 Debugging

### Enable Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
```

### Common Issues

1. **API Key Not Found**
   - Check `.env` file exists
   - Verify key is correctly formatted
   - Ensure `load_dotenv()` is called

2. **Module Import Errors**
   - Check virtual environment is activated
   - Reinstall requirements: `pip install -r requirements.txt`
   - Verify PYTHONPATH includes project root

3. **API Rate Limits**
   - Implement exponential backoff
   - Add retry logic
   - Cache responses when appropriate

## 📊 Performance Optimization

### Caching Responses

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_explain(topic, audience):
    return buddy.explain(topic, audience)
```

### Batch Processing

```python
# Process multiple topics efficiently
async def batch_async(topics, audience):
    tasks = [
        async_explain(topic, audience)
        for topic in topics
    ]
    return await asyncio.gather(*tasks)
```

## 🔐 Security Considerations

1. **Never commit API keys**
2. **Validate user input** (especially for API)
3. **Rate limit endpoints** (use libraries like `slowapi`)
4. **Sanitize outputs** (prevent prompt injection)
5. **Use HTTPS** in production

## 📚 Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic API Docs](https://docs.anthropic.com)
- [Gradio Documentation](https://gradio.app/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Typer Documentation](https://typer.tiangolo.com)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Ensure all tests pass
5. Update documentation
6. Submit a pull request

## 📧 Support

For questions or issues:
- Open a GitHub issue
- Check existing documentation
- Review example code

---

Happy developing! 🚀
