FROM apache/airflow:3.2.0

USER root
# Instalar dependencias del sistema operativo si hicieran falta
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

ARG EXTRA_REQUIREMENTS=""

RUN if [ -n "$EXTRA_REQUIREMENTS" ]; then \
    pip install --no-cache-dir $EXTRA_REQUIREMENTS ; \
    fi

RUN pip install --no-cache-dir gunicorn apache-airflow-providers-celery

WORKDIR /opt/airflow