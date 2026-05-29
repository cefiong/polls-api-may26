# Use python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in docker container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .


# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5001


# Run the application
CMD ["python", "app.py"]