# DottyBot

## Python Requirements

[pillow](https://pillow.readthedocs.io/en/stable/)
[numpy](https://www.numpy.org/)
[discord](https://discordpy.readthedocs.io/en/latest/)
[json-logging](https://pypi.org/project/json-logging/)


## Environment

```
BOT_TOKEN=<your bot token>
```


## Run Locally

```
git clone https://github.com/mieux2/dottybot.git
cd dottybot
python setup.py install
dottybot runbot
```


## Run with Docker

```
git clone https://github.com/mieux2/dottybot.git
cd dottybot
./build-docker.sh
docker run -it --env "BOT_TOKEN=$BOT_TOKEN" dotbot:latest-dev dottybot runbot
```
