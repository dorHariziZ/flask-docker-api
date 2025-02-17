FROM python:3.11-slim

WORKDIR /app
COPY . /app/
COPY ./vendor /app/vendor

ENV PYTHONPATH="/app/vendor"

CMD ["python", "server.py"]
