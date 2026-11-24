import random

print("Welcome to Python AI Chatbot!")
print("You can start chatting with me.")
print("Type 'bye' to exit.\n")

responses = {
    "hello": ["Hello! How are you?", "Hi there! Nice to meet you!"],
    "how are you": ["I am doing great! How about you?",
                    "I'm fine. Thanks for asking!"],
    "name": ["I am PyBot, your virtual assistant!"],
    "weather": ["I cannot check live weather, but I hope it is sunny!"],
    "python": ["Python is a popular programming language."],
    "study": ["Keep learning! Practice makes you better."],
    "bye": ["Goodbye! Have a great day!", "See you again!"]
}

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for keyword in responses:
        if keyword in user_input:
            print("Bot:", random.choice(responses[keyword]))
            found = True
            break

    if not found:
        print("Bot: Interesting! Can you tell me more?")