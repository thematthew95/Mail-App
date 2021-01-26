FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
RUN apt update && apt install -y gcc
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
