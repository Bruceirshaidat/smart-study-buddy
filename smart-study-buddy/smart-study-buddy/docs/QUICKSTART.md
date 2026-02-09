# 🚀 Quick Start Guide - Smart Study Buddy

Get started with Smart Study Buddy in 5 minutes!

## Option 1: Local Setup (Recommended)

### Step 1: Clone and Setup

```bash
# Clone repository
git clone https://github.com/yourusername/smart-study-buddy.git
cd smart-study-buddy

# Run setup script
chmod +x setup.sh
./setup.sh

# Or manual setup:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Configure API Keys

Edit `.env` file:

```env
OPENAI_API_KEY=sk-your-key-here
```

### Step 3: Try It Out!

```bash
# Quick test
python -c "from src.study_buddy import explain_for_child; print(explain_for_child('how airplanes fly'))"

# Run examples
python examples/run_examples.py

# Start web interface
python web_app.py
# Open http://localhost:7860
```

## Option 2: Google Colab (No Installation)

1. Click: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/smart-study-buddy/blob/main/notebooks/Smart_Study_Buddy.ipynb)

2. Add your API key in the second cell

3. Run all cells and start learning!

## Option 3: VS Code

### Setup in VS Code

1. Open folder in VS Code
2. Install Python extension
3. Select Python interpreter (from venv)
4. Create `.env` with your API key
5. Run any Python file

### Quick Commands

```bash
# Terminal in VS Code
python examples/run_examples.py
python cli.py interactive
python web_app.py
```

## 🎯 Your First Explanation

### Using Python

```python
from src.study_buddy import SmartStudyBuddy

buddy = SmartStudyBuddy()

# Explain to a child
print(buddy.explain("gravity", "child"))

# Explain to an expert
print(buddy.explain("quantum entanglement", "expert"))
```

### Using CLI

```bash
# Basic
python cli.py explain "photosynthesis" --audience middle_school

# Advanced
python cli.py explain "blockchain" \
    --audience intermediate \
    --tone professional \
    --length detailed
```

### Using Web UI

```bash
python web_app.py
```

Then open browser to http://localhost:7860

## 📚 Common Use Cases

### 1. Explaining to Kids

```python
from src.study_buddy import explain_for_child

topics = ["clouds", "rainbows", "stars", "dinosaurs"]
for topic in topics:
    print(f"\n{topic.upper()}:")
    print(explain_for_child(topic))
```

### 2. Study Aid for Students

```python
buddy = SmartStudyBuddy()

# Middle school science
print(buddy.explain("cell division", "middle_school", length="medium"))

# High school physics
print(buddy.explain("Newton's laws", "high_school", tone="academic"))
```

### 3. Professional Development

```python
buddy = SmartStudyBuddy()

# Learn new tech
print(buddy.explain("Kubernetes", "beginner", tone="professional"))

# Deep dive
print(buddy.explain("microservices architecture", "intermediate", length="detailed"))
```

### 4. Batch Learning

```bash
# CLI batch mode
python cli.py batch "React,Vue,Angular,Svelte" --audience beginner

# Python
buddy = SmartStudyBuddy()
frameworks = ["React", "Vue", "Angular"]
for fw in frameworks:
    print(buddy.explain(f"{fw} framework", "beginner"))
```

## 🎨 Customization Tips

### Choose the Right Audience

- `child` - Use for actual 5-year-olds or when you want maximum simplicity
- `elementary` - Good for ages 6-10 or basic introductions
- `middle_school` - Ages 11-14, structured learning
- `high_school` - Ages 15-18, more academic
- `beginner` - Adults new to a topic
- `intermediate` - Some background knowledge
- `advanced` - Substantial background
- `expert` - Deep expertise

### Choose the Right Tone

- `playful` - Fun, imaginative, great for kids or making dry topics interesting
- `neutral` - Balanced, straightforward, safe default
- `academic` - Formal, structured, for studying
- `professional` - Business-appropriate, technical

### Choose the Right Length

- `short` - Quick overview, 1-2 paragraphs
- `medium` - Balanced explanation, 3-5 paragraphs (default)
- `detailed` - Comprehensive, 6+ paragraphs

## 🔧 Troubleshooting

### "API key not found"

Make sure `.env` file exists and contains:
```env
OPENAI_API_KEY=your_key_here
```

### "Module not found"

```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### "OpenAI API error"

- Check your API key is valid
- Ensure you have credits/billing enabled
- Check your internet connection

## 📊 Next Steps

1. ✅ Try different topics and audiences
2. ✅ Experiment with tones and lengths
3. ✅ Build your own learning curriculum
4. ✅ Share with students or colleagues
5. ✅ Contribute improvements!

## 💡 Tips for Best Results

1. **Be specific with topics**: "photosynthesis in plants" vs "photosynthesis"
2. **Match audience to actual level**: Don't use "expert" unless you really are one
3. **Try different tones**: Same topic can feel very different with different tones
4. **Compare levels**: Generate same topic for child, beginner, and expert to see adaptation
5. **Use batch mode**: Efficient for learning multiple related topics

## 🆘 Need Help?

- 📖 Read the full [README.md](README.md)
- 🐛 Report issues on GitHub
- 💬 Check the examples in `examples/`
- 📓 Try the Jupyter notebook

## 🎉 Have Fun Learning!

Smart Study Buddy is designed to make learning accessible and enjoyable for everyone. Experiment, explore, and discover!
