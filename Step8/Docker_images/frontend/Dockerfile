FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
COPY frontend.py .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask psycopg2-binary

EXPOSE 5001

CMD ["python", "frontend.py"]
