FROM python:3.9.10

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

CMD ["uvicorn", "FastAPI-main.app:app", "--host", "0.0.0.0", "--port", "7860"]