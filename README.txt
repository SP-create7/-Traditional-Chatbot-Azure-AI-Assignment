# Traditional Student Help Chatbot with Azure AI

## Project Overview

This project demonstrates the development of a traditional rule-based chatbot enhanced with Microsoft Azure AI Language Service for sentiment analysis.

The chatbot answers predefined university-related questions and uses Azure AI to analyze the sentiment of user messages that are not part of its predefined knowledge base.

The project was developed using Python in Visual Studio Code and Azure AI Language Service.

---

## Features

- Rule-based chatbot
- University information assistant
- Azure AI Sentiment Analysis
- Handles unknown questions gracefully
- Simple command-line interface
- GitHub source control

---

## Technologies Used

- Python 3.11
- Microsoft Azure AI Language Service
- Azure AI Text Analytics SDK
- Visual Studio Code
- GitHub

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Traditional-Chatbot-Project.git
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the chatbot

```bash
python traditional_chatbot_project.py
```

---

## Supported Commands

- hello
- help
- office hours
- library
- fees
- contact
- bye

For all other inputs, Azure AI performs sentiment analysis.

---

## Example

User:

```
I love studying Artificial Intelligence.
```

Output

```
Detected Sentiment: positive

Bot: You sound happy and positive!
```

---

## Azure AI Integration

The chatbot connects to Microsoft Azure AI Language Service using the Azure Text Analytics SDK.

The chatbot:

- Sends unknown text to Azure
- Receives sentiment analysis
- Responds according to Positive, Neutral or Negative sentiment

---

## Project Structure

```
Traditional-Chatbot-Project/
│
├── traditional_chatbot_project.py
├── Traditional_Chatbot_Project.ipynb
├── requirements.txt
├── README.md
└── Screenshots/
```

---

## Author

Student Project

University of the Cumberlands

---

## License

This project was developed for educational purposes.