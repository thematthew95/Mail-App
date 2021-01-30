FROM python:3.9.1-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . /code/
CMD ["python3", "mail-app.py"]
