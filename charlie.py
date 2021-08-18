from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Training Example')

#trainer = ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("./custom.json")
#trainer.train(
#    "chatterbot.corpus.custom.myown"
#)

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Bonjour')

print(response)
