FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-traditional
RUN apt-get update && apt-get install -y gettext

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN chown -R appuser:appuser /app
RUN chmod +x /app/entrypoint.sh

USER appuser

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]