FROM ubuntu:18.04
MAINTAINER William M Mortl <wimortl@microsoft.com>

# open the port for SSL
EXPOSE 8080

# environment vars
ENV hellomessage=helloworld!

# install dependencies
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install -y python3 python3-pip

# make the logging directory
RUN mkdir -p /var/log/TestFlaskService/

# create directories and add files
ADD src /TestFlaskService

# pip installs
RUN pip3 install -r /TestFlaskService/requirements.txt

WORKDIR /TestFlaskService
CMD ["python3", "test-flask-service.py"]
