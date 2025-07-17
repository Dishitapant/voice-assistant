import random

def answer_query(command):
    default_responses = [
        "That's interesting. I'll have to think about it.",
        "I'm not sure, but I can learn!",
        "Hmm... I'm still getting smarter every day.",
        "Can you rephrase that for me?",
        "Let me search that online for you."
    ]
    return random.choice(default_responses)