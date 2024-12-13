FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Necessario per lo sviluppo di un bot in python
ENV PYTHONUNBUFFERED=1 

CMD ["python", "main.py"]