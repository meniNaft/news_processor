import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from app.external_api.groq_api import post_groq_api
from app.external_api.news_api import fetch_news
from app.services.kafka_service.producer import producer_send_message

load_dotenv(verbose=True)
NEWS_TOPIC = os.environ["NEWS_TOPIC"]


def main_processor():
    current_time = datetime.now()
    next_iteration_time = current_time + timedelta(minutes=2)
    counter = 1
    while True:
        news = fetch_news(counter)
        for index, elem in enumerate(news):
            print("index: ", index)
            res = post_groq_api(elem)
            if res and res['category'] != 'general':
                additional_info = {key: elem[key] for key in ["date", "title", "body"] if key in elem}
                produced_object = {**res, **additional_info}
                print(datetime.now(), "produced_object is sent")
                producer_send_message(NEWS_TOPIC, produced_object, key=str(counter))
        counter += 1
        remaining_time = (next_iteration_time - datetime.now()).total_seconds()
        if remaining_time > 0:
            time.sleep(remaining_time)
