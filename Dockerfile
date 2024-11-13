#FROM python:3.12
FROM dockerproxy.repos.tech.orange/python:3.12

#ENV APP_HOME /app
#WORKDIR $APP_HOME

ARG PORT=8080
ARG API_URL
ENV PORT=$PORT API_URL=${API_URL:-http://localhost:$PORT}


RUN apt-get update -y && apt-get install -y caddy && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs=18.17.0-1nodesource1

RUN node -v && npm -v

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

#RUN groupadd -r app && useradd -r -g app app
#COPY --chown=app:app . ./
#USER app

#HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

#ENTRYPOINT ["reflex", "run", "--env", "prod", "--loglevel", "debug" ]

RUN reflex init

RUN reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web
STOPSIGNAL SIGKILL
EXPOSE $PORT
CMD caddy start && reflex run --env prod --backend-only --loglevel debug
