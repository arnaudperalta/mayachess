go build -o mayachess src/*.go
chmod 777 mayachess
mv mayachess ../lichess-bot/engines/main
cd ../lichess-bot
python3 lichess-bot.py -u -v
