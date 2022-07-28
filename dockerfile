# powerful image, not need to set nginx
FROM nginx/unit:1.23.0-python3.9

LABEL maintainer="Qi Li <rance.liki@gmail.com>"

COPY ./config/config.json /docker-entrypoint.d/config.json
COPY . /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update  \
    && apt install -y python3-pip  \
    && pip3 install -r requirements.txt \
    && python -m spacy download en_core_web_sm \
    && python -m spacy download en_core_web_md

RUN apt remove -y python3-pip  \
    && apt autoremove --purge -y  \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

EXPOSE 8000