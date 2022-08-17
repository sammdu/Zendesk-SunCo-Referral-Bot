# Zendesk-SunCo-Referral-Bot

Telegram/SunCo chatbot to demonstrate the `conversation:referral` feature of the Sunshine Conversations Engine (SunCo) at Zendesk.

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

First, you must configure the following required environment variables:

-   `SUNCO_BASE_URL`: base URL for the SunCo API, including protocol and FQDN, but without a trailing slash
    -   e.g. `https://example.zendesk.com`
-   `SUNCO_AUTH_KEYID`: the ID of an API key used for authentication with the SunCo API
-   `SUNCO_AUTH_SECRET`: the secret associated with the above key ID
-   `SUNCO_BOT_NAME`: the display name for this chat bot

You can run the app using Flask's built-in development server like so:

```bash
flask run
```

Note that this server is not suitable for production use.

Visit the app at: http://localhost:5000
