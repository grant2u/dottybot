FROM python:3 AS build

ENV APP_HOME /app
ENV PATH $APP_HOME/bin:$PATH
COPY . $APP_HOME/src
COPY config.json $APP_HOME/etc/config.json
COPY scripts/tobraille.py $APP_HOME/bin/tobraille
COPY scripts/runbot.py $APP_HOME/bin/runbot
WORKDIR $APP_HOME/src

RUN pip install --upgrade pip -e .

ENTRYPOINT ["runbot"]
