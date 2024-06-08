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

ENV GDAL_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu/libgdal.so
ENV LD_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu

# Set work directory
WORKDIR /code

# Install dependencies
COPY ../../dependencies/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY ../.. /code/

# Create the staticfiles directory
RUN mkdir -p /code/staticfiles

# Set the entrypoint
ENTRYPOINT ["/code/compose/api/entrypoint.sh"]