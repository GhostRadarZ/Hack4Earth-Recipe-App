# Dockerfile for the Recipe App Backend

# A Dockerfile must begin with a FROM clause. The Docker Hub registry has pre-built images.
# We are pulling a Python image, specifying the Python version as well as the Debian version
FROM python:3.11.5-bookworm

# The ARG instruction defines a variable that users can pass at build-time
ARG PORT=8000

# ENV sets the environment variables inside the container
ENV PORT $PORT

# WORKDIR creates the directory and changes it to the current working directory
WORKDIR /recipe-app/backend

# RUN is an image build step
# First we update the package manager and install necessary packages
RUN apt-get update && apt-get install -y \
    libzbar0

# Copies over the requirements file to the image
COPY requirements.txt requirements.txt

# Installs all necessary Python packages
RUN pip install -r requirements.txt

# Copy the source code from the host to the image
# We do this at the end as it frequently changes
COPY . .

# Exposes the given port
EXPOSE $PORT

# Runs a command after the image is built
# This runs the backend server
CMD uvicorn api:app --host 0.0.0.0 --port $PORT --reload
