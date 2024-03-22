from flask import Flask, render_template, request
import nltk
nltk.download('punkt')
from textblob import TextBlob
from newspaper import Article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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
