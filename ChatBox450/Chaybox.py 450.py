#Kerin.Quintero
#Ctech450
#2/20/23

import spacy
nlp = spacy.load("en_core_web_sm")

def greet(context):
    """Display a greeting message to the user based on context."""
    if not context.get("greeted"):
        print("Hello! Welcome to Quinteros' Bakery Chatbot!")
        print("I'm here to help you with your questions or orders about our bakery.")
        print("Type 'exit' or 'quit' anytime to end the conversation.\n")
        context["greeted"] = True  # Mark that the user has been greeted
    else:
        print("Hello again! How can I assist you further at Quinteros' Bakery?")

def get_user_input():
    """Get input from the user."""
    return input("You: ")

def process_input(user_input):
    doc = nlp(user_input)
    


def identify_intent(user_input):
    """Identify the user's intent based on the input text."""
    text = user_input.lower()
    # Check for greeting intents, including the slang 
    greetings = ["hi", "hello", "hey", "greetings", "yo", "wasgood"]
    for word in greetings:
        if word in text:
            return "greeting"
        
        # Check for departure/goodbye intents
    departures = ["bye", "goodbye", "see you", "farewell", "later", "exit", "quit"]
    for word in departures:
        if word in text:
            return "goodbye"
    
    # Check for specific product options
    if "cookie" in text:
        return "cookies"
    if "cake" in text:
        return "cakes"
    if "pastry" in text:
        return "pastries"
    if "bread" in text:
        return "breads"
    # Other intents
    if "order" in text or "buy" in text:
        return "order"
    elif "hours" in text or "open" in text:
        return "hours"
    elif "menu" in text or "item" in text:
        return "menu"
    elif "location" in text or "address" in text:
        return "location"
    else:
        return "unknown"

def generate_response(intent):
    """Generate a response based on the user's intent."""
    if intent == "greeting":
        return "Hello there! How can I help you today?"
    elif intent == "order":
        return "Sure, I'd be happy to help you place an order. What treat from Quinteros' Bakery would you like?"
    elif intent == "hours":
        return "Our bakery is open from 7 AM to 7 PM Monday through Saturday, and 8 AM to 4 PM on Sundays."
    elif intent == "menu":
        return "We offer a variety of breads, pastries, cakes, and cookies. Which item interests you?"
    elif intent == "location":
        return "Quinteros' Bakery is located at 123 Main Street. Would you like directions?"
    elif intent == "unknown":
        return "I'm sorry, I didn't understand that. Could you please rephrase your question or command?"
    else:
        return "I'm sorry, something went wrong."

def close_conversation():
    """Display a closing message to the user."""
    print("\nThank you for visiting Quinteros' Bakery Chatbot. Have a great day!")

def chatbot():
    # start of the conversation
    context = {}
    
    # Use context to greet the user appropriately
    greet(context)
    
    while True:
        user_input = get_user_input()
        
        # Check if the user wants to end the conversation
        if user_input.lower() in ["exit", "quit"]:
            close_conversation()
            break
        
        # Identify the user's intent and store it in context for future interactions
        intent = identify_intent(user_input)
        context["last_intent"] = intent
        
        # Generate and display the bot's response
        response = generate_response(intent)
        print("Chatbot:", response)

if __name__ == '__main__':
    chatbot()
