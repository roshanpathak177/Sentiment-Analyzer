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
            if sentiment > 0:
                color = 'green'
            else:
                color = 'red'
            return render_template('index.html', color=color)
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')
