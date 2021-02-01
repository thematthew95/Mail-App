FROM python:3.9.1-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /code && \
	pip3 install python-decouple && \
	apt update && \
	apt -y install nginx
WORKDIR /code
COPY . /code/
ENTRYPOINT ["python3", "mail-app.py"]
