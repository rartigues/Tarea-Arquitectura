# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Copy requirements.txt into the Docker image
COPY requirements.txt ./

# Install the application's dependencies in the Docker image
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the Docker image
COPY . .

# Expose the port that the application listens on
EXPOSE 8000

# Define the command to run the application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
