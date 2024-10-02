# Pull base image
FROM python:3.11.4-slim-buster

# Set env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APP_HOME=/home/app

#Set work dir
WORKDIR $APP_HOME

# Copy the entire source code directory to the container
COPY ./src .

# Copy requirements.txt
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install wkhtmltopdf
RUN apt-get update && apt-get install -y wkhtmltopdf xvfb

# Expose port
EXPOSE 8000
