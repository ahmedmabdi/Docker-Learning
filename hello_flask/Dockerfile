# stage 1
FROM python:3.8-slim as Build 

WORKDIR /app

# Install system-level dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install flask mysqlclient

# stage 2
FROM python:3.8-slim
WORKDIR /app
COPY --from=Build /app /app

EXPOSE 5002

CMD ["python", "app.py"]