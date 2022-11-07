FROM python:2.7-slim
ENV APP /log_demo
WORKDIR $APP
RUN mkdir log
COPY ./main.py .
EXPOSE 8080
CMD ["python","main.py"]
