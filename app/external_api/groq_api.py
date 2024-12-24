import json
import os
from typing import Any
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

load_dotenv(verbose=True)

GROQ_API_KEY = os.environ["GROQ_API_KEY"]

expected_schema = {
    "body": str,
    "title": str,
    "lat": float,
    "lon": float,
    "date": datetime.date,
    "category": str,
}


def post_groq_api(article_content: dict) -> Any | None:
    client = Groq(api_key=GROQ_API_KEY)

    try:
        chat_completion = client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": (
                    f"{json.dumps(article_content)}\n\n"
                    "This is an article. I want to analyze a few things:\n"
                    "1. Extract the city mentioned in the article.\n"
                    "2. Provide the latitude and longitude of that city.\n"
                    "3. Classify the article into one of the following categories: general, history, news.\n\n"
                    "After analyzing, respond with a JSON that contains the following fields:\n"
                    "{\n"
                    "    \"category\": \"str\",\n"
                    "    \"city\": \"str\",\n"
                    "    \"lat\": \"float\",\n"
                    "    \"lon\": \"float\"\n"
                    "}\n\n"
                    "Respond with the JSON only, without any extra text."
                ),
            }],
            model="llama3-8b-8192",
        )

        response = json.loads(chat_completion.choices[0].message.content)
        return {
            "category": response.get("category", ""),
            "city": response.get("city", ""),
            "lat": response.get("lat", 0.0),
            "lon": response.get("lon", 0.0)
        }

    except Exception as e:
        print(f"Error processing the response: {e}")
        return None
