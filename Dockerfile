FROM python:3.9

LABEL maintainer="Qi Li <rance.liki@gmail.com>"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:5000", "wsgi:app"]