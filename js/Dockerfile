FROM node:8
MAINTAINER William M Mortl <wimortl@microsoft.com>

# open the port
EXPOSE 8080

# create directories and add files
ADD src /testservice

# install requirements and build
RUN cd /testservice && npm install
RUN cd /testservice && npm build

WORKDIR /testservice
CMD ["npm", "start"]
