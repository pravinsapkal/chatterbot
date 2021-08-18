# Importing chatterbot
from chatterbot import ChatBot

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Buddy',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

# Inport ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

# Now we can export the data to a file
#trainer.export_for_training('./my_export.json')
#trainer.export_for_training('./export.yml')

# Get a response to the input text 'I would like to book a flight.'
response = bot.get_response('language?')

print("Bot Response:", response)
