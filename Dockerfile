#FROM python:3
FROM debian:11

USER root
WORKDIR /usr/src/app

COPY requirements.txt .
RUN apt-get update
RUN apt-get install -y python3
RUN python3 --version
RUN apt-get install -y python3-pip
RUN pip3 install  -r requirements.txt 

COPY . .

CMD ["python3", "cat_lovers_VS_dog_lovers.py"]
