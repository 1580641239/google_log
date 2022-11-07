FROM python:2.7-slim
COPY ./main.py ./
CMD ["mkdir" "log"]
EXPOSE 8080
CMD ["python","main.py"]
