#!/usr/bin/env

from enum import Enum
from flask import Flask, render_template, make_response, Response, request
import os
import requests
from typing import Optional, Literal

app = Flask(__name__)


API_PARAMS: dict = {
    "base_url": os.environ["SUNCO_BASE_URL"],
    "headers": {"User-Agent": "Python/3.10.6"},
    "auth_user": os.environ["SUNCO_AUTH_KEYID"],
    "auth_pass": os.environ["SUNCO_AUTH_SECRET"],
}

BOT_DISPLAY_NAME: str = os.environ["SUNCO_BOT_NAME"]


class SuncoEventType(Enum):
    create: str = "conversation:create"
    referral: str = "conversation:referral"
    message: str = "conversation:message"


@app.route("/")
def hello_world() -> str:
    """
    Webpage with Telegram Referral Link
    """
    return render_template("index.html")


@app.route("/sunco-create-referral", methods=["POST"])
def sunco_create_referral() -> Response:
    """
    Webhook Receiver Endpoint
    """
    body: Optional[dict] = request.get_json()

    if request.method == "POST" and body:
        app_id: Optional[str] = body.get("app", {}).get("id")
        first_event: dict = events[0] if (events := body.get("events")) else {}
        event_type: Optional[SuncoEventType] = SuncoEventType(first_event.get("type"))
        convo_id: Optional[str] = (
            first_event.get("payload", {}).get("conversation", {}).get("id")
        )
        user_id: Optional[str] = get_user_id_from_event(first_event, event_type)

        print()
        print(f"App ID: {app_id}")
        print(f"Event type: {event_type.value if event_type else None}")
        print(f"Convo ID: {convo_id}")
        print(f"User ID: {user_id}")
        print()

        assert app_id is not None
        assert convo_id is not None
        if event_type == SuncoEventType.create:
            respond_to_sunco_message("Howdy pardner!", "text", app_id, convo_id)
        elif event_type == SuncoEventType.referral:
            respond_to_sunco_message("Not you again!", "text", app_id, convo_id)

    return make_response("ok", 200)


def get_user_id_from_event(
    event: dict, event_type: Optional[SuncoEventType]
) -> Optional[str]:
    if event_type in {SuncoEventType.create, SuncoEventType.referral}:
        return event.get("payload", {}).get("user", {}).get("id")
    elif event_type == SuncoEventType.message:
        return (
            event.get("payload", {})
            .get("message", {})
            .get("author", {})
            .get("user", {})
            .get("id")
        )
    return None


def respond_to_sunco_message(
    content: str, message_type: Literal["text", "image"], app_id: str, convo_id: str
):
    url: str = (
        f'{API_PARAMS["base_url"]}/v2/apps/{app_id}/conversations/{convo_id}/messages'
    )
    data: dict = {
        "author": {"type": "business", "displayName": BOT_DISPLAY_NAME},
        "content": {"type": message_type},
        "metadata": {"lang": "en-ca"},
    }

    if message_type == "text":
        data["content"]["text"] = content
    elif message_type == "image":
        data["content"]["mediaUrl"] = content

    requests.post(
        url,
        auth=(str(API_PARAMS["auth_user"]), str(API_PARAMS["auth_pass"])),
        json=data,
        headers=API_PARAMS["headers"],
    )
