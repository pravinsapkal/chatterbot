import os
from flask import Flask, render_template, request
from urllib.parse import urlparse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#english_bot = ChatBot('Examplebot', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri=urlparse(os.environ.get('DATABASE_URL')))
trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")
trainer.train("./custom.json")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
