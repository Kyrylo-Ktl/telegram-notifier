FROM python:3.10-slim-buster

# Setup environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV WORKDIR /app

# Establishing working directory
WORKDIR $WORKDIR

# Copy source code
COPY . ${WORKDIR}

# Install dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Run example on container startup
CMD ["python", "example.py"]
