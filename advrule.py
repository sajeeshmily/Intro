
import random
from datetime import datetime

# Store conversation history
chat_history = []

# Predefined chatbot responses
responses = {
    "hello": [
        "Hello! Nice to meet you!",
        "Hi there! How can I help you?",
        "Hey! Welcome to SmartBot!"
    ],

    "how are you": [
        "I am doing great! Thanks for asking.",
        "I am fine. How about you?"
    ],

    "your name": [
        "My name is SmartBot.",
        "I am SmartBot, your virtual assistant."
    ],

    "python": [
        "Python is a popular programming language.",
        "Python is easy to learn and powerful."
    ],

    "ai": [
        "AI stands for Artificial Intelligence.",
        "AI helps computers perform intelligent tasks."
    ],

    "thank": [
        "You are welcome!",
        "Happy to help!",
        "Anytime!"
    ],

    "bye": [
        "Goodbye! Have a wonderful day!",
        "See you again!"
    ]
}


# Function to display welcome message
def welcome():
    print("=" * 40)
    print("       WELCOME TO SMARTBOT")
    print("=" * 40)

    print("I am your virtual assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'exit' to end the conversation.\n")


# Function to process user input
def chatbot_response(message):

    message = message.lower().strip()

    # Check greetings
    if "hello" in message or "hi" in message:
        return random.choice(responses["hello"])

    # Check predefined questions and keywords
    for keyword in responses:

        if keyword in message:
            return random.choice(responses[keyword])

    # Check date and time
    if "time" in message:
        return "Current time: " + datetime.now().strftime("%I:%M %p")

    if "date" in message:
        return "Today's date: " + datetime.now().strftime("%d-%m-%Y")

    # Default response
    return "Interesting! Can you explain that in another way?"


# Function to display conversation history
def show_history():

    print("\n--- CHAT HISTORY ---")

    if len(chat_history) == 0:
        print("No conversation available.")

    else:
        for chat in chat_history:
            print(chat)


# Function to display help
def show_help():

    print("\n--- AVAILABLE COMMANDS ---")
    print("help    - Display commands")
    print("history - View conversation history")
    print("clear   - Clear conversation history")
    print("time    - Display current time")
    print("date    - Display today's date")
    print("exit    - Exit chatbot")


# Main chatbot program
welcome()

while True:

    user_input = input("You: ").strip()

    # Handle empty input
    if user_input == "":
        print("Bot: Please enter something.")
        continue

    command = user_input.lower()

    # Exit command
    if command in ["exit", "bye", "quit"]:
        print("Bot:", random.choice(responses["bye"]))
        break

    # Help command
    elif command == "help":
        show_help()
        continue

    # History command
    elif command == "history":
        show_history()
        continue

    # Clear history
    elif command == "clear":
        chat_history.clear()
        print("Bot: Conversation history cleared!")
        continue

    # Generate response
    else:

        bot_reply = chatbot_response(user_input)

        print("Bot:", bot_reply)

        # Store conversation
        chat_history.append("You: " + user_input)
        chat_history.append("Bot: " + bot_reply)

print("\nThank you for chatting with SmartBot!")
print("Total interactions:", len(chat_history) // 2)
