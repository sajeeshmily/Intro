
from textblob import TextBlob
from colorama import Fore, init

init(autoreset=True)

# Store sentiment statistics
stats = {
    "Positive": 0,
    "Negative": 0,
    "Neutral": 0
}

# Store conversation history
history = []

# Function to analyze sentiment
def analyze_sentiment(message):

    analysis = TextBlob(message)
    score = analysis.sentiment.polarity

    if score > 0:
        sentiment = "Positive"
        print(Fore.GREEN + "Positive sentiment detected! 😊")

    elif score < 0:
        sentiment = "Negative"
        print(Fore.RED + "Negative sentiment detected! 😟")

    else:
        sentiment = "Neutral"
        print(Fore.YELLOW + "Neutral sentiment detected! 😐")

    print("Sentiment Score:", round(score, 2))

    return sentiment


# Function to display statistics
def show_stats():

    print(Fore.CYAN + "\n--- SENTIMENT STATISTICS ---")

    total = sum(stats.values())

    print("Total Messages:", total)

    for key, value in stats.items():
        print(key, ":", value)


# Function to display history
def show_history():

    print(Fore.CYAN + "\n--- CONVERSATION HISTORY ---")

    if len(history) == 0:
        print("No messages recorded.")

    else:
        for item in history:
            print(item)


# Function to reset data
def reset_data():

    for key in stats:
        stats[key] = 0

    history.clear()

    print(Fore.YELLOW + "All data has been reset!")


# Function to generate final report
def final_report():

    print(Fore.CYAN + "\n================================")
    print("       FINAL SENTIMENT REPORT")
    print("================================")

    show_stats()

    print(Fore.GREEN + "\nThank you for using Sentiment Spy!")
    print("Mission Completed!")


# Main chatbot
print(Fore.CYAN + "================================")
print("       SENTIMENT SPY")
print("================================")

print(Fore.GREEN + "Welcome, Detective!")
print("Enter a message to analyze its sentiment.")

print("\nAvailable Commands:")
print("stats - View statistics")
print("history - View conversation history")
print("reset - Reset collected data")
print("help - View commands")
print("exit - Generate final report")

while True:

    message = input(Fore.CYAN + "\nYou: ").strip()

    if not message:
        print(Fore.YELLOW + "Please enter a message.")
        continue

    command = message.lower()

    if command == "exit":
        final_report()
        break

    elif command == "stats":
        show_stats()

    elif command == "history":
        show_history()

    elif command == "reset":

        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":
            reset_data()
        else:
            print("Reset cancelled.")

    elif command == "help":

        print("stats, history, reset, help, exit")

    else:

        sentiment = analyze_sentiment(message)

        # Update statistics
        stats[sentiment] += 1

        # Save conversation
        history.append(message + " --> " + sentiment)
