FROM python:3.8

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .
COPY main.py .


CMD ["python", "main.py"]