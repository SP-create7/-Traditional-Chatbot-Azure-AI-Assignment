# ==========================================
# Student Help Chatbot with Azure AI
# Traditional Rule-Based Chatbot
# Integrated with Azure AI Language Service
# ==========================================

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# ==========================================
# Azure AI Configuration
# ==========================================

endpoint = "https://chatbot-language-service-spatha47468.cognitiveservices.azure.com/"
key = "F3PaybdBfhZBHLqO8jzrqREltWujrs9PKomLVRPwXzTfxBiRT2AGJQQJ99CGAC1i4TkXJ3w3AAAaACOGuUiz"

credential = AzureKeyCredential(key)

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=credential
)

# ==========================================
# Function to Analyze Sentiment
# ==========================================

def analyze_sentiment(text):
    documents = [text]

    response = client.analyze_sentiment(documents=documents)[0]

    return response.sentiment

# ==========================================
# Welcome Screen
# ==========================================

print("==========================================")
print(" Welcome to the Student Help Chatbot ")
print("==========================================")
print("This chatbot uses Azure AI Sentiment Analysis.")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

# ==========================================
# Chatbot Loop
# ==========================================

while True:

    question = input("You: ").strip().lower()

    if question == "hello":
        print("Bot: Hello! How can I help you today?")

    elif question == "help":
        print("\nBot: I can answer the following questions:")
        print("---------------------------------------")
        print("hello")
        print("office hours")
        print("library")
        print("fees")
        print("contact")
        print("bye")
        print("\nFor any other message, I will use Azure AI to analyze your sentiment.\n")

    elif question == "office hours":
        print("Bot: The university offices are open Monday to Friday from 8:00 AM to 5:00 PM.")

    elif question == "library":
        print("Bot: The university library is open daily from 8:00 AM to 10:00 PM.")

    elif question == "fees":
        print("Bot: Please contact the Finance Office for tuition and payment information.")

    elif question == "contact":
        print("Bot: Email: support@university.edu")

    elif question == "bye":
        print("Bot: Goodbye! Have a wonderful day!")
        break

    else:

        try:

            sentiment = analyze_sentiment(question)

            print("\nAzure AI Sentiment Analysis")
            print("---------------------------")
            print("Detected Sentiment:", sentiment)

            if sentiment == "positive":
                print("Bot: You sound happy and positive! 😊")

            elif sentiment == "negative":
                print("Bot: It sounds like you're having a difficult time. I hope things improve.")

            else:
                print("Bot: Your message sounds neutral.")

        except Exception as e:
            print("Bot: Unable to connect to Azure AI.")
            print("Error:", e)

        print("\nBot: Sorry, I don't have a predefined answer for that question.\n")
        print("Bot: However, Azure AI detected that your message has a", sentiment, "sentiment.\n")