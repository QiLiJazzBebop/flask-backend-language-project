FROM python:3.7.13

LABEL maintainer="Qi Li <rance.liki@gmail.com>"

COPY . /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

EXPOSE 5000
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_md