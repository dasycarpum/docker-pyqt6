# Use Ubuntu as the base image
FROM ubuntu:23.10

# Combine ENV statements
ENV DEBIAN_FRONTEND=noninteractive \
    LIBGL_ALWAYS_INDIRECT=1 \
    QT_DEBUG_PLUGINS=1

# Add user
RUN apt-get update && apt-get install -y adduser \
    && adduser --quiet --disabled-password --gecos '' qtuser \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Python 3 and PyQt6
RUN apt-get update && apt-get install -y \
    python3-pyqt6 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Copy the application code into the container
COPY src/ ./src/

# Set the main script as the container's entrypoint
CMD ["python3", "./src/main.py"]
