FROM python:3.11-slim AS builder

RUN addgroup --system appgroup && adduser --system --group app
RUN pip install gunicorn
WORKDIR /app

COPY . .

RUN chown -R app:app /app

RUN pip install --no-cache-dir -r requirements.txt

USER app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "phone-combinations:app"]