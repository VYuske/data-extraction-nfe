# docker build -t data-extraction-nfe . --rm
# docker run -p 8501:8501 --device /dev/video0:/dev/video0 data-extraction-nfe

# Base image with Python 3.10
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg libsm6 libxext6 zbar-tools \
    curl \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives

# Copy your project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port if using Streamlit or Flask
EXPOSE 8501

# Default command to run the app (update if needed)
CMD ["streamlit", "run", "application/main.py"]