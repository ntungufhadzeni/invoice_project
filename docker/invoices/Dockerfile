# Pull base image
FROM python:3.11.4-slim-buster

RUN apt-get update \
    && apt-get -y install build-essential libpq-dev \
    && apt-get clean

# Install wkhtmltopdf
RUN apt-get update && apt-get install -y wkhtmltopdf xvfb --fix-missing

# Set env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APP_HOME=/home/project

#Set work dir
WORKDIR $APP_HOME

# Copy the entire source code directory to the container
COPY ./src .

# Copy requirements.txt
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000
