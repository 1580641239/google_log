FROM python:2.7-slim
COPY ./main.py ./
EXPOSE 8080
CMD ["python","app.py"]
