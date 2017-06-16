FROM ubuntu:16.04
MAINTAINER "nicolas@atakama.io"

RUN apt-get update
RUN apt-get -y install \
  wget \
  python-setuptools \
  python-dev \
  build-essential \
  git

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

COPY ./requirements.txt py_fxengine/
WORKDIR py_fxengine/
RUN pip install -r requirements.txt

RUN mkdir /var/log/py_fxengine
ENV RABBIT_USERNAME tonyg
ENV RABBIT_PASSWORD changeit
ENV RABBIT_HOST 54.246.180.253
ENV RABBIT_PORT 5672
