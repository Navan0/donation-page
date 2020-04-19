#Base python slim
FROM python:3.6-slim

# Installing base packages
RUN apt-get -y update && apt-get install wget unzip gcc tar -y

# Copy files to container
COPY . /app

# Set working directory
WORKDIR /app

# Upgrade PIP
RUN pip install --upgrade pip

# Install the project and dependencies
RUN pip install -e .


RUN chmod +x /app/ops/run.gunicorn.sh

# Run the web server
CMD /app/ops/run.gunicorn.sh