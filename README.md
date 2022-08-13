# Zendesk-SunCo-Referral-Bot

Chatbot to demonstrate the `conversation:referral` feature of the Sunshine Conversations Engine at Zendesk.

### :book: [Official Documentation for Conversation Referrals](https://docs.smooch.io/guide/conversation-referrals/)

## Setup

Create a Python virtual environment:

```bash
python3.10 -m venv env_referral
```

Clone this repository:

```bash
git clone https://github.com/sammdu/Zendesk-SunCo-Referral-Bot.git
```

Enter the repository and enable the virtual environment:

```bash
cd Zendesk-SunCo-Referral-Bot
source ../env_referral/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the App Server

You can run the app using Flask's built-in development server like so:

```bash
flask run
```

Note that this server is not suitable for production use.

Visit the app at: http://localhost:5000
