from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('CHOTTU')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/prave/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
                        data=open('C:/Users/prave/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
                        bot.train(data)

                        
while True:
       message=input('you:')
       if message.strip!='Bye' or message.strip!='bye':
         reply=bot.get_response(message)
         print('Chatbot:',reply)
       if message.strip=='Bye' or message.strip=='bye':
         print('chatbot:If was nice talking to you')
         break
