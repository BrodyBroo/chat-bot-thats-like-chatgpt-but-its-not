from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
  'CodeCopilotBot',
  logic_adapters = [
    'chatterbot.logic.BestMatch',
    'chatterbot.logic.TimeLogicAdapter'
  ]
)

trainer = ListTrainer(chatbot)

#Training Data
conversations = [
  "Hello",
  "Hi there!",
  "How are you?",
  "I'm good, thanks for asking!",
  "What's your name?",
  "I'm CodeCopilotBot, your friendly chatbot."
]

trainer.train(converstations)

print("ChatBot is ready to talk! Type 'exit' to end the converstation.")
while True:
  user_input = input("You: ")
  if user_input.lower() == 'exit':
    print("Goodbye!")
    break
  response = chatbot.get_response(user_input)
  print("CodeCopilotBot: ", response)
