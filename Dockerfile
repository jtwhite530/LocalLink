FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD ["gunicorn", "locallink_project.wsgi:application", "--bind", "0.0.0.0:8000"]
