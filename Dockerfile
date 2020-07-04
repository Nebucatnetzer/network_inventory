FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip install wheel
RUN pip install -r requirements/docker.txt
CMD ["/bin/bash", "/code/run.sh"]
