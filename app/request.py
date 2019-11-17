from app import app
import urllib.request,json
from .models import news



News = news.News

# Getting the api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

def get_news(id):
    '''
    Function that gets the sources url
    '''
    get_news_url = NEWS_API_BASE_URL.format(id,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_object = None

        if get_news_response:
            self.id = id
            self.name = name
            self.description = description
            self.url = url
            self.category = category
            self.language = language
            self.country = country 

    return news_results
    
    
def process_results(news_list):
    '''
    function that processes the news result
    '''
    news_results = []
    for news_item in news_results_list:

        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)

    return news_results
