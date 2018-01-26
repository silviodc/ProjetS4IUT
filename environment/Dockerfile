# Use an official Python runtime as a parent image
FROM python:3.6

# Set the file requirement
ADD requirements.txt ./

ARG http_proxy
ARG https_proxy
ARG no_proxy

RUN export http_proxy=$http_proxy \
  && export https_proxy=$https_proxy \
  && export no_proxy=$no_proxy

RUN echo http_proxy

RUN echo https_proxy

# Install any needed packages specified in requirements.txt
RUN apt-get update
RUN apt-get install -y python-pip python-dev libmysqlclient-dev
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8899

# Set the working directory to /twitter
RUN mkdir /twitter
WORKDIR /twitter

# Define environment variable
ENV MYSQL_DB_HOST MYSQL_ROOT_PASSWORD MYSQL_DATABASE MYSQL_USER

# Run app.py when the container launches
CMD ["python", "app.py"]
