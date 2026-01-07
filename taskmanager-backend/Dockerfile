FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ENV PYTHONPATH=/app


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN pytest -v

EXPOSE 5000

CMD ["gunicorn", "-b","0.0.0.0:5000", "wsgi:app"]
