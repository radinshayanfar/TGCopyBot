FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip

ADD ./requirements.txt /app/
RUN python3 -m pip install -r /app/requirements.txt

ADD ./main.py /app/
