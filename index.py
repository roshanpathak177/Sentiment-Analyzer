import os
import nltk

os.environ['nltk_data'] = os.path.join(os.path.dirname(__file__), 'nltk_DATA')

from flask import Flask, render_template, request
from textblob import TextBlob
from newspaper import Article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(nltk.data.find('tokenizers/punkt'))
    if request.method == 'POST':
        url = request.form['url']
        article = Article(url)
        try:
            article.download()
            article.parse()
            article.nlp()
            text = article.summary
            obj = TextBlob(text)
            sentiment = obj.sentiment.polarity
            print(f"Sentiment Polarity: {sentiment}")
            if sentiment > 0:
                body_class = 'positive-body'
            else:
                body_class = 'negative-body'
            return render_template('index.html', body_class=body_class, polarity=sentiment)
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')
