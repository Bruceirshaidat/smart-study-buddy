# 🎓 Smart Study Buddy

> An adaptive AI tutor that explains any topic perfectly matched to your audience's age, level, and background.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 🎯 **Adaptive Explanations**: Automatically adjusts complexity based on audience level
- 👶 **8 Audience Levels**: From 5-year-old children to domain experts
- 🎨 **Multiple Tones**: Playful, neutral, academic, or professional
- 📏 **Flexible Length**: Short summaries to detailed deep-dives
- 🤖 **Dual AI Support**: Works with both OpenAI and Anthropic APIs
- 💻 **Multiple Interfaces**: CLI, Web UI, Python API, and Jupyter notebooks
- ⚡ **Streaming Support**: Real-time response generation
- 🎪 **Rich Output**: Beautiful formatted terminal output with Rich library

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-study-buddy.git
cd smart-study-buddy

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file or set environment variables:

```bash
# OpenAI (primary)
OPENAI_API_KEY=your_openai_key_here

# Anthropic (optional)
ANTHROPIC_API_KEY=your_anthropic_key_here

# Pinecone (optional, for future features)
PINECONE_API_KEY=your_pinecone_key_here
```

### 3. Run Examples

```bash
# Python script
python examples/run_examples.py

# CLI
python cli.py explain "quantum physics" --audience child

# Web interface
python web_app.py
```

## 📖 Usage

### Python API

```python
from src.study_buddy import SmartStudyBuddy

# Initialize
buddy = SmartStudyBuddy(provider="openai")

# Basic usage
explanation = buddy.explain(
    topic="photosynthesis",
    audience="middle_school"
)

# With all options
explanation = buddy.explain(
    topic="machine learning",
    audience="intermediate",
    tone="professional",
    length="detailed"
)

# Quick helpers
from src.study_buddy import explain_for_child, explain_for_expert

print(explain_for_child("black holes"))
print(explain_for_expert("neural networks"))
```

### Command Line Interface

```bash
# Basic explanation
python cli.py explain "gravity" --audience elementary

# With options
python cli.py explain "blockchain" \
    --audience intermediate \
    --tone professional \
    --length detailed \
    --provider openai

# Interactive mode
python cli.py interactive

# Batch processing
python cli.py batch "gravity,photosynthesis,DNA" --audience middle_school

# List available options
python cli.py list-options
```

### Web Interface (Gradio)

```bash
python web_app.py
```

Then open http://localhost:7860 in your browser.

### Jupyter Notebook

Open `notebooks/Smart_Study_Buddy.ipynb` in Jupyter or Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/smart-study-buddy/blob/main/notebooks/Smart_Study_Buddy.ipynb)

## 🎯 Audience Levels

| Level | Description | Example Use Case |
|-------|-------------|------------------|
| `child` | 5-year-old | Simple concepts with fun metaphors |
| `elementary` | Ages 6-10 | Basic science and everyday topics |
| `middle_school` | Ages 11-14 | Structured learning with examples |
| `high_school` | Ages 15-18 | Academic preparation and depth |
| `beginner` | Adult novice | Professional development, new hobbies |
| `intermediate` | Some knowledge | Building on existing foundation |
| `advanced` | Strong background | Technical depth and nuance |
| `expert` | Domain expert | Latest research, edge cases, theory |

## 🎨 Customization Options

### Tones
- **playful**: Fun, engaging, uses humor and imagination
- **neutral**: Balanced, straightforward explanations
- **academic**: Formal, structured, scholarly
- **professional**: Business-appropriate, technical when needed

### Lengths
- **short**: Quick overview (1-2 paragraphs)
- **medium**: Balanced explanation (3-5 paragraphs)
- **detailed**: Comprehensive deep-dive (6+ paragraphs)

## 📁 Project Structure

```
smart-study-buddy/
├── src/
│   ├── ai_client.py        # AI provider interface
│   ├── prompts.py           # System prompts and templates
│   └── study_buddy.py       # Main application class
├── notebooks/
│   └── Smart_Study_Buddy.ipynb  # Colab notebook
├── examples/
│   └── run_examples.py      # Example usage
├── tests/
│   └── test_study_buddy.py  # Unit tests
├── cli.py                   # Command-line interface
├── web_app.py              # Gradio web interface
├── requirements.txt         # Dependencies
├── .env                     # API keys (create this)
├── .gitignore
└── README.md
```

## 🔧 Advanced Features

### Streaming Responses

```python
# Stream word-by-word
for chunk in buddy.explain(topic, audience, stream=True):
    print(chunk, end="")
```

### Batch Processing

```python
topics = ["gravity", "photosynthesis", "DNA"]
results = buddy.batch_explain(topics, audience="middle_school")
```

### Conversation History

```python
# Get history
history = buddy.get_history()

# Clear history
buddy.clear_history()
```

### Custom Models

```python
# Use specific OpenAI model
buddy = SmartStudyBuddy(provider="openai", model="gpt-3.5-turbo")

# Use Claude
buddy = SmartStudyBuddy(provider="anthropic", model="claude-sonnet-4-20250514")
```

## 🧪 Examples

### Example 1: Explaining to a Child

**Input:**
```python
buddy.explain("how computers work", audience="child", tone="playful")
```

**Output:**
> Imagine a computer is like a super-smart friend who can follow instructions really, really fast! When you press a button or touch the screen, you're giving your computer friend a job to do...

### Example 2: Expert Level

**Input:**
```python
buddy.explain("quantum entanglement", audience="expert", tone="academic")
```

**Output:**
> Quantum entanglement represents a fundamental non-classical correlation between quantum systems, arising from the superposition principle and described mathematically by entangled states that cannot be factored into independent subsystems...

## 🛠️ Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/ cli.py web_app.py
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Use Cases

- 🎓 **Education**: Teachers adapting lessons for different grade levels
- 👨‍👩‍👧 **Parents**: Explaining complex topics to curious kids
- 💼 **Corporate Training**: Onboarding at different skill levels
- 📚 **Self-Learning**: Understanding new topics at your own pace
- ♿ **Accessibility**: Making knowledge accessible to all backgrounds
- 🌍 **Tutoring**: Personalized explanations for students

## 🔐 Security

- Never commit `.env` files
- API keys are loaded from environment variables
- Use `.gitignore` to prevent accidental commits
- Consider using secrets management for production

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Acknowledgments

- Built with [OpenAI](https://openai.com) and [Anthropic](https://anthropic.com) APIs
- UI powered by [Gradio](https://gradio.app)
- CLI built with [Typer](https://typer.tiangolo.com) and [Rich](https://rich.readthedocs.io)

## 📧 Contact

Questions or suggestions? Open an issue or reach out!

---

**Made with ❤️ by the Smart Study Buddy team**
