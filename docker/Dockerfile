####
# This Dockerfile is used in order to build a container that runs the Spring Boot application
#
# Build the image with:
#
# docker build -f docker/Dockerfile -t python/sample-basic .
#
# Then run the container using:
#
# docker run -i --rm -p 8081:8081 python/sample-basic
####
# FROM python:latest
FROM registry.access.redhat.com/ubi8/python-38:latest


# Add application sources with correct permissions for OpenShift
USER 0
#ADD app-src .
WORKDIR /projects

RUN chown -R 1001:0 ./
USER 1001


RUN python3 -m venv venv
RUN . venv/bin/activate

# optimize image caching
COPY requirements.txt .
RUN pip install -U "pip>=19.3.1" && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8081
CMD [ "waitress-serve", "--port=8081", "app:app"]
