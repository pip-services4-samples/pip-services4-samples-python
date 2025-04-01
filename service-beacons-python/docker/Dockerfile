FROM python:3.9-slim-buster

# Install git for adding dependecies from git
RUN apt-get update && apt-get -y install git

# Set working directory
WORKDIR /app

# Copy project file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all project
COPY . .

ENV HTTP_PORT=8080
ENV MONGO_SERVICE_HOST=
ENV MONGO_SERVICE_PORT=27017

EXPOSE "8080:8080"
CMD [ "python", "bin/main.py" ]

