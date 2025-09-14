# Dockerfile (Lambda)
FROM public.ecr.aws/lambda/python:3.11

# Fast logs + sane defaults for DuckDB/MotherDuck in Lambda
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    LOCAL_DB=/tmp/f1.duckdb \
    DUCKDB_EXTENSION_DIRECTORY=/tmp/duckdb_extensions \
    HOME=/tmp \
    PYTHONPATH=/var/task:/var/task/utils

# /var/task is the Lambda working directory
WORKDIR /var/task

# Install Python deps first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY extract/ extract/
COPY load/ load/
COPY utils/ utils/
COPY app.py .
COPY config.py .

# Lambda will call app.lambda_handler
CMD ["app.lambda_handler"]
