from flask import render_template
from app import app
from .request import get_news

# Views

@app.route('/')
def index():
    '''
    View news page function that returns the news details page and its data
    '''

    # Getting general news

    general_news = get_news('general')
    # print(general_news)
    entertainment_news = get_news('entertainment')
    business_news = get_news('business')


    title = 'Home - Welcome to Our News Online Appplication'

    return render_template('index.html', title = title, general = general_news, entertainment = entertainment_news, business = business_news)