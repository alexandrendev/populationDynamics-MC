FROM python:3.12.3-slim

WORKDIR /app

COPY ./src/rafikov /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]

