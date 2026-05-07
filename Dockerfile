FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Create input and output directories
RUN mkdir -p /input/logs
RUN mkdir -p /output

# Run inference script
CMD ["python", "inference.py"]
