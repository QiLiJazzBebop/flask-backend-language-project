FROM python:3.9

LABEL maintainer="Qi Li <rance.liki@gmail.com>"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_md
CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:5000", "wsgi:app"]