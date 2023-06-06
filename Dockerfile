FROM python:3.10-slim

WORKDIR /backend

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
