from app import app
import urllib.request,json
from .models import news


News = news.News

# Getting the api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(sources):
    '''
    Function that gets the sources url
    '''
    get_news_url = base_url.format(sources,api_key)

    with_urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results