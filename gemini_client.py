import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# SSL verification disabled for hackathon environments
http_client = httpx.Client(verify=False, timeout=60)

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"


def guardrail_input(text):
    blocked_words = ["password", "secret", "api key"]
    for word in blocked_words:
        if word in text.lower():
            raise Exception("Blocked sensitive query")
    return text


def guardrail_output(text):
    if len(text) > 5000:
        text = text[:5000]
    return text


PROMPT_TEMPLATE = """
You are an expert DevOps Incident Analysis AI.

Use ONLY provided context.

Context:
{context}

Question:
{question}

Provide structured answer:

Root Cause:
Impact:
Resolution:
Prevention:
"""


def call_gemini(context, question):

    question = guardrail_input(question)

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    headers = {
        "Content-Type": "application/json"
    }

    params = {
        "key": GEMINI_API_KEY
    }

    json_data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = http_client.post(
        GEMINI_URL,
        headers=headers,
        params=params,
        json=json_data
    )

    result = response.json()

    output = result["candidates"][0]["content"]["parts"][0]["text"]

    output = guardrail_output(output)

    return output
