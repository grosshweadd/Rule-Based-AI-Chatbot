import random
from datetime import datetime

print("🤖 AI Chatbot")
print("Type 'bye' to exit.\n")

greetings = [
    "Hello! Nice to meet you.",
    "Hi there! How can I help you today?",
    "Hey! What's up?"
]

while True:
    user = input("You: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking. How are you?")

    elif "your name" in user:
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif "who made you" in user or "your master" in user:
        print("Bot: I was developed by Akshat Asthana.")

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    elif "study" in user:
        print("Bot: Consistent practice and revision are key to learning.")

    elif "python" in user:
        print("Bot: Python is a beginner-friendly programming language used in AI, web development, and data science.")

    elif "java" in user:
        print("Bot: Java is an object-oriented programming language widely used for enterprise applications.")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that typically require human intelligence.")

    elif "weather" in user:
        print("Bot: I can't check live weather, but you can use a weather app or website.")

    elif "hobby" in user:
        print("Bot: My hobby is chatting with users and answering questions!")

    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "motivate" in user:
        print("Bot: Success comes from consistent effort. Keep learning and improving every day!")

    elif "goal" in user:
        print("Bot: Setting clear and achievable goals is a great way to stay focused.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: I'm sorry, I don't understand that yet. Can you ask something else?")
