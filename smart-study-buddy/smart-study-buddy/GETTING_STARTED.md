# ✅ Getting Started Checklist

Complete these steps to start using Smart Study Buddy in under 5 minutes!

## 📥 Step 1: Download & Setup

- [ ] Download the entire `smart-study-buddy` folder
- [ ] Open terminal/command prompt
- [ ] Navigate to the folder: `cd smart-study-buddy`

## 🔧 Step 2: Install Dependencies (Choose One)

### Option A: Automatic Setup (Recommended)
```bash
chmod +x setup.sh
./setup.sh
```

### Option B: Manual Setup
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ✅ Step 3: Verify API Keys

Your API keys are already in `.env`:
- [ ] OpenAI API key: ✓ Configured
- [ ] Pinecone API key: ✓ Configured  
- [ ] Secret key: ✓ Configured

## 🎯 Step 4: Test the Installation

Try one of these commands:

```bash
# Quick test (Python one-liner)
python -c "from src.study_buddy import explain_for_child; print(explain_for_child('clouds'))"

# Interactive demo
python demo.py

# Example scripts
python examples/run_examples.py

# Web interface
python web_app.py
# Then open http://localhost:7860

# Command line
python cli.py explain "photosynthesis" --audience child
```

## 🎪 Step 5: Explore Features

### Try Different Audiences
```bash
python cli.py explain "gravity" --audience child
python cli.py explain "gravity" --audience expert
```

### Try Different Tones
```bash
python cli.py explain "AI" --audience beginner --tone playful
python cli.py explain "AI" --audience intermediate --tone professional
```

### Batch Processing
```bash
python cli.py batch "DNA,proteins,cells" --audience middle_school
```

## 📚 Step 6: Learn More

- [ ] Read `README.md` for full documentation
- [ ] Check `docs/QUICKSTART.md` for more examples
- [ ] Review `docs/DEVELOPMENT.md` if you want to extend it
- [ ] Try the Jupyter notebook in `notebooks/`

## 🌐 Step 7: Choose Your Interface

### For Web UI Lovers
```bash
python web_app.py
```

### For CLI Enthusiasts
```bash
python cli.py --help
```

### For Developers
```bash
python api_server.py
# API docs at http://localhost:8000/docs
```

### For Jupyter/Colab Users
- Open `notebooks/Smart_Study_Buddy.ipynb`
- Or upload to Google Colab

## 🎨 Step 8: Customize (Optional)

### Change AI Model
Edit `.env` and modify:
```env
DEFAULT_MODEL=gpt-4o        # Most capable
# or
DEFAULT_MODEL=gpt-3.5-turbo # Faster, cheaper
```

### Add Anthropic/Claude
```env
ANTHROPIC_API_KEY=your_key_here
```

Then in code:
```python
buddy = SmartStudyBuddy(provider="anthropic")
```

## ✨ You're Ready!

### Quick Commands Reference

```bash
# Demo with all features
python demo.py

# Simple explanation
python cli.py explain "TOPIC" --audience LEVEL

# Web interface
python web_app.py

# API server
python api_server.py

# Examples
python examples/run_examples.py

# Tests
pytest tests/
```

### Python Quick Reference

```python
from src.study_buddy import SmartStudyBuddy

buddy = SmartStudyBuddy()

# Basic
buddy.explain("topic", "audience")

# Full options
buddy.explain(
    topic="your topic",
    audience="beginner",  # or child, expert, etc.
    tone="neutral",       # or playful, academic, professional
    length="medium"       # or short, detailed
)
```

## 🎉 Success Criteria

You'll know it's working when:
- ✅ No import errors
- ✅ API calls succeed
- ✅ Explanations are generated
- ✅ Different audiences get different explanations
- ✅ Web UI loads (if using web_app.py)

## 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| "Module not found" | Run `pip install -r requirements.txt` |
| "API key error" | Check `.env` file, verify key is correct |
| "Permission denied" (setup.sh) | Run `chmod +x setup.sh` first |
| "Port in use" | Change port in code or kill other process |

## 📊 What to Try First

1. **Total Beginner?** → `python demo.py` (option 6 - Interactive)
2. **Want Quick Results?** → `python cli.py explain "gravity" --audience child`
3. **Prefer GUI?** → `python web_app.py`
4. **Developer?** → Check out `api_server.py` and `docs/DEVELOPMENT.md`
5. **Notebook Person?** → Open `notebooks/Smart_Study_Buddy.ipynb`

---

## 🎯 Your First Real Use

### Example 1: Explain to Your Kids
```python
from src.study_buddy import explain_for_child

topics = ["stars", "rainbows", "why sky is blue", "dinosaurs"]
for topic in topics:
    print(f"\n=== {topic.upper()} ===")
    print(explain_for_child(topic))
```

### Example 2: Learn Something New
```python
from src.study_buddy import SmartStudyBuddy

buddy = SmartStudyBuddy()

# Start at beginner level
print(buddy.explain("quantum computing", "beginner"))

# Once comfortable, level up
print(buddy.explain("quantum entanglement", "intermediate"))
```

### Example 3: Teaching Tool
```bash
# Create explanations for different grade levels
python cli.py batch "photosynthesis,cells,DNA" --audience elementary > elementary_biology.txt
python cli.py batch "photosynthesis,cells,DNA" --audience high_school > highschool_biology.txt
```

---

**You're all set! Choose a starting point above and begin exploring. Have fun! 🚀**
