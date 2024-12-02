import spacy
import random

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define intents with patterns and responses
intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "greetings", "what's up"],
        "responses": ["Hello! How can I help you?", "Hi there! What can I do for you?", "Hey! How are you doing?"]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you later", "quit"],
        "responses": ["Goodbye! Have a great day!", "See you next time!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "I appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
    },
    "help": {
        "patterns": ["help", "assist", "support"],
        "responses": ["Sure! Let me know how I can assist you.", "I'm here to help! What do you need?"]
    },
    "default": {
        "responses": ["I'm sorry, I didn't understand that. Could you rephrase?", "Can you clarify?"]
    }
}

def preprocess_text(text):
    """
    Preprocess user input using spaCy.
    """
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

def match_intent(user_input):
    """
    Match user input to an intent based on predefined patterns.
    """
    processed_input = preprocess_text(user_input)
    for intent, data in intents.items():
        for pattern in data.get("patterns", []):
            if pattern in processed_input:
                return intent
    return "default"

def get_response(intent):
    """
    Get a random response for the matched intent.
    """
    return random.choice(intents[intent]["responses"])

def chatbot():
    """
    Run the chatbot interaction loop.
    """
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        intent = match_intent(user_input)
        response = get_response(intent)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chatbot()
