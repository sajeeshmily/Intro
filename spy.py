from textblob import TextBlob
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

print(Fore.CYAN + "================================")
print(Fore.YELLOW + "       SENTIMENT SPY")
print(Fore.CYAN + "================================")

print(Fore.GREEN + "Welcome, Detective!")
print(Fore.WHITE + "Your mission is to detect emotions.")
print(Fore.YELLOW + "Type 'exit' to end the mission.\n")

while True:

    message = input(Fore.CYAN + "You: ")

    if message.lower() == "exit":
        print(Fore.YELLOW + "\nMission Completed!")
        print(Fore.GREEN + "Goodbye, Detective!")
        break

    # Analyze the message
    analysis = TextBlob(message)

    score = analysis.sentiment.polarity

    print(Fore.WHITE + "\n--- SENTIMENT REPORT ---")

    if score > 0:
        print(Fore.GREEN + "Emotion: POSITIVE ")
        print(Fore.GREEN + "Spy Feedback: Excellent! Positive vibes detected!")

    elif score < 0:
        print(Fore.RED + "Emotion: NEGATIVE ")
        print(Fore.RED + "Spy Feedback: Warning! Negative vibes detected!")

    else:
        print(Fore.YELLOW + "Emotion: NEUTRAL ")
        print(Fore.YELLOW + "Spy Feedback: No strong emotion detected.")

    print(Fore.CYAN + "Sentiment Score: " + str(round(score, 2)))

    print(Fore.WHITE + "------------------------\n")