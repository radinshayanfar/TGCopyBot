FROM python:3.10-slim-bullseye

WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY app .

CMD ["python", "main.py"]
