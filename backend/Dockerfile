# 1. Use lightweight Python image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies (if needed later)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements first (layer caching)
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code
COPY . .

# 7. Expose FastAPI port
EXPOSE 8000

# 8. Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

