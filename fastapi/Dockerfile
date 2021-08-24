FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7



ADD /api /app/api
ADD /core /app/core
ADD /models /app/models
ADD /services /app/services
ADD /utils /app/utils
ADD main.py /app/main.py
ADD __init__.py /app/__init__.py
ADD requeriments.txt /app/requeriments.txt

ADD drenv.env /app/drenv.env

RUN pip install -r /app/requeriments.txt
