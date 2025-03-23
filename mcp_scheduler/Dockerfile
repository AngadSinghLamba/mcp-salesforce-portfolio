# Use Python base image
FROM python:3.10

# Set working directory in container
WORKDIR /app

# Copy all local files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

