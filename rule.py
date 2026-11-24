
print("================================")
print("       PYTHON CHATBOT")
print("================================")

print("Hello! I am PyBot.")
print("You can chat with me.")
print("Type 'bye' to exit.\n")

while True:

    message = input("You: ").lower()

    if "hello" in message or "hi" in message:
        print("Bot: Hello! Nice to meet you!")

    elif "how are you" in message:
        print("Bot: I am doing great! Thanks for asking.")

    elif "your name" in message:
        print("Bot: My name is PyBot.")

    elif "python" in message:
        print("Bot: Python is a popular programming language.")

    elif "weather" in message:
        print("Bot: I hope you are enjoying the weather!")

    elif "thank" in message:
        print("Bot: You are welcome!")

    elif "help" in message:
        print("Bot: Sure! How can I help you?")

    elif "bye" in message:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand. Can you ask something else?")
