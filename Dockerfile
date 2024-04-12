# Use the official Python image as a base image
FROM python:3.11-slim-bookworm

# Set environment variables for Poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION="1.8.2"

# Install necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Copy only the requirements files to work directory
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
