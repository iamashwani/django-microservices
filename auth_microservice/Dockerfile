# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /auth_microservice

# Copy the current directory contents into the container at /app
COPY . /auth_microservice/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that the Django app will listen on

