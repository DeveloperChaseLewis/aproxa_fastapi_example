FROM python:3.9.10-slim-buster

WORKDIR /src

#Copy requirements.txt over so we can pip install
COPY requirements.txt /src

#Install pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt