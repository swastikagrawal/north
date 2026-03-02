from groq import Groq
from openai import OpenAI
import settings
import database
import time 

def build_message_for_api(history, new_message):
    messages = []
    messages.append({"role": "system", "content": settings.SYSTEM_PROMPT})
    for msg in history:
        if msg["role"] == "User":
            messages.append({"role": "user", "content": msg["message"]})
        else:
            messages.append({"role": "assistant", "content": msg["message"]})
    messages.append({"role": "user", "content": new_message})
    return messages


def stream_response(user_message):
    history = database.get_last_n_messages()
    database.save_message("User", user_message)

    full_response = ""

    try:
        client = Groq(api_key=settings.GROQ_API_KEY)
        messages = build_message_for_api(history, user_message)

        stream = client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=messages,
            stream=True,
        )

        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text is None:
                text = ""
            full_response = full_response + text
            yield text

        database.save_message("North", full_response)

    except Exception:

        full_response = ""

        try:
            client = OpenAI(api_key=settings.OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")
            messages = build_message_for_api(history, user_message)

            stream = client.chat.completions.create(
                model=settings.OPEN_ROUTER_MODEL,
                messages=messages,
                stream=True,
            )

            for chunk in stream:
                text = chunk.choices[0].delta.content
                if text is None:
                    text = ""
                full_response = full_response + text
                yield text

            database.save_message("North", full_response)

        except Exception as e:
            print("North is temporarily unavailable, please try again later.")
            time.sleep(10)
            quit()
            return