# Use a minimal Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install prometheus_client

COPY . .

# Expose the port your app runs on
EXPOSE 8081

# Run the app
CMD ["python", "app.py"]
