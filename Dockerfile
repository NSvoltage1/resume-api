# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# Make port 5000 available to the world outside the container
EXPOSE 5000

# Define the command to run your app using gunicorn or simply python
# For example: 
CMD ["python", "app.py"]


