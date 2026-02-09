#!/bin/bash

# Smart Study Buddy - Setup Script

echo "🎓 Setting up Smart Study Buddy..."
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Check for .env file
if [ ! -f .env ]; then
    echo ""
    echo "⚠️  .env file not found!"
    echo "Creating .env template..."
    cat > .env << EOF
# API Keys for Smart Study Buddy
OPENAI_API_KEY=your_openai_key_here
# ANTHROPIC_API_KEY=your_anthropic_key_here
# PINECONE_API_KEY=your_pinecone_key_here

# Model Configuration
DEFAULT_MODEL=gpt-4o
MAX_TOKENS=2000
TEMPERATURE=0.7
EOF
    echo "✓ Created .env template"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your API keys!"
else
    echo ""
    echo "✓ .env file exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your API keys"
echo "2. Run examples: python examples/run_examples.py"
echo "3. Try CLI: python cli.py explain 'photosynthesis' --audience child"
echo "4. Start web UI: python web_app.py"
echo ""
echo "For Jupyter: jupyter notebook notebooks/Smart_Study_Buddy.ipynb"
echo ""
