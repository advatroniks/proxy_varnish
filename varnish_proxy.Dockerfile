FROM python:3.11-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install poetry

WORKDIR /home/api/application

COPY pyproject.toml /home/api/application

RUN poetry install

COPY . .

EXPOSE 80

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]