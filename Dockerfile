FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip install wheel
RUN pip install -r requirements.txt
WORKDIR /code/network_inventory
