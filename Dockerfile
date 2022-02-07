# Python 3.9.6
FROM python@sha256:736b76eb3f64778646ce0051fb5fed4dfbf67016e51563946230ca8bb40ac687
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip install wheel
RUN pip install -r requirements/docker.txt
CMD ["/bin/bash", "/code/run.sh"]
