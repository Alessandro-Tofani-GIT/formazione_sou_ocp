FROM python:3.10-slim

WORKDIR /app

COPY backend.py .

RUN pip install flask psycopg2-binary

EXPOSE 5001

CMD ["python", "backend.py"]

