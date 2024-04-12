# 'Dockerfile'
#
# Create a Docker image to run the EvoAI web service 
#
# Copyright (c) 2016-2023 EncoreSky Ltd. All rights reserved.

# Use slim python image
FROM python:3.8.11-slim
# Install git, gcc and python dev for header files
RUN apt-get update
# Copy the Python dependencies file
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# Upgrade pip and install the Python dependencies
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

# Copy everything needed to the working directory
COPY ./flask_boilerplate  /app/flask_boilerplate
COPY ./.env  /app/.env
COPY ./run.py  /app/run.py

CMD ["python", "run.py"]