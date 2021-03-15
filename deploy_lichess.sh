cd src
pyinstaller --onefile main.py
cd dist
chmod 777 main
mv main ../../../lichess-bot/engines/main
cd ../../../lichess-bot
python3 lichess-bot.py -u -v
