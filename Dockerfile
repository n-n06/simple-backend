FROM python:3.11

RUN mkdir -p /usr/app/src
WORKDIR /usr/app

COPY ./requirements.txt /usr/app

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY src/ usr/app/src

EXPOSE 8000
CMD ["fastapi", "run", "src/main.py", "--port", "8000"]
