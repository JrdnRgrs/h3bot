docker rm -f h3bot
#docker build -t h3bot --build-arg bot_token=$env:TOKEN --build-arg booster_channel=$env:booster_channel --build-arg mod_channel=$env:mod_channel --build-arg booster_name=$env:booster_name --build-arg mod_name=$env:mod_name github.com/JrdnRgrs/h3bot
docker build -t h3bot --build-arg bot_token=$TOKEN --build-arg booster_channel=$booster_channel --build-arg mod_channel=$mod_channel --build-arg booster_name=$booster_name --build-arg mod_name=$mod_name github.com/JrdnRgrs/h3bot
docker run -d --name h3bot h3bot