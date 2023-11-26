# Use Ubuntu as the base image
FROM ubuntu:23.10

# Combine ENV statements
ENV DEBIAN_FRONTEND=noninteractive \
    LIBGL_ALWAYS_INDIRECT=1 \
    QT_DEBUG_PLUGINS=1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Python 3 and PyQt6
RUN apt-get update && apt-get install -y \
    python3-pyqt6 \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code into the container
COPY src/ ./src/

# Set the main script as the container's entrypoint
CMD ["python3", "./src/main.py"]