FROM docker.io/gorialis/discord.py:latest
ARG bot_token
ENV bot_token=$bot_token

ARG booster_channel="937516569909674024"
ENV booster_channel=$booster_channel

ARG mod_channel="937719522805301330"
ENV mod_channel=$mod_channel

ARG booster_name="Server Booster"
ENV booster_name=$booster_name

ARG mod_name="Moderator"
ENV mod_name=$mod_name

COPY h3bot.py /mnt/
ENTRYPOINT ["python", "/mnt/h3bot.py"]