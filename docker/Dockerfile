# Build from the python base image using the amd64 version
FROM --platform=linux/amd64 python:3.8-slim

# Work from now inside the /app folder
WORKDIR /app

# Install all the depencies of the project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application inside the image
COPY . .

# Declare that the image listen on the port 5000
EXPOSE 5000

# This is the process that will be run
CMD ["python", "app.py"]