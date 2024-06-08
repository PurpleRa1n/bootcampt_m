FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gdal-bin \
    libgdal-dev \
    build-essential \
    gcc \
    netcat-openbsd \
    && apt-get clean

# Dynamically find the GDAL library path
RUN if [ -f /usr/lib/aarch64-linux-gnu/libgdal.so ]; then \
      export GDAL_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu/libgdal.so && \
      export LD_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu; \
    elif [ -f /usr/lib/x86_64-linux-gnu/libgdal.so ]; then \
      export GDAL_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgdal.so && \
      export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu; \
    else \
      echo "GDAL library not found"; \
      exit 1; \
    fi

# Set work directory
WORKDIR /code

# Install dependencies
COPY ../../dependencies/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY ../.. /code/

# Ensure the entrypoint script has execution permissions
RUN chmod +x /code/compose/api/entrypoint.sh

# Create the staticfiles directory
RUN mkdir -p /code/staticfiles

# Set the entrypoint
ENTRYPOINT ["/code/compose/api/entrypoint.sh"]
