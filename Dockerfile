FROM python:3.7

RUN apt-get update -y && \
    apt-get install -y python3-pip

RUN pip3 install pip --upgrade
RUN pip3 install --no-cache-dir loguru
RUN pip3 install --no-cache-dir flask

ENV APP /test_demo
WORKDIR $APP
RUN mkdir log
COPY ./app.py .
EXPOSE 80
CMD ["python","app.py"]
