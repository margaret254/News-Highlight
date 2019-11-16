from flask import render_template
from app import app

# Views

@app.route('/news/<int:news_id>')
def index():
    '''
    View news page function that returns the news details page and its data
    '''

    title = 'Home - Welcome to Our News Online Appplication'

    return render_template('index.html', title = title)