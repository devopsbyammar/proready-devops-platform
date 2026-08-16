# Build stage
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install  --no-cache-dir --target=/install -r requirements.txt


# Final stage
FROM python:3.12-slim

WORKDIR /app
COPY --from=builder /install /usr/local/lib/python3.12/site-packages
COPY . .

RUN useradd -m appuser && chown -R appuser /app

USER appuser

EXPOSE 5001

CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:5001", "app:app"]
