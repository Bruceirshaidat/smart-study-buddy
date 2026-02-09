# Smart Study Buddy - Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create .env from environment variables at runtime
# (API keys should be passed as environment variables)

# Expose ports
EXPOSE 7860 8000

# Default command (can be overridden)
CMD ["python", "web_app.py"]

# Alternative commands:
# docker run <image> python cli.py explain "topic" --audience child
# docker run -p 8000:8000 <image> python api_server.py
