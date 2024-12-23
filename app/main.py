from app.services.kafka_service.admin import init_topics
from app.services.main_news_handler import main_processor

if __name__ == '__main__':
    init_topics()
    main_processor()
