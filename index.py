import os
import tempfile
import nltk

# Create a temporary directory for NLTK data
temp_dir = tempfile.TemporaryDirectory()

# Download the required NLTK data to the temporary directory
nltk.download('punkt', download_dir=temp_dir.name)

# Set the NLTK data directory to the temporary directory
nltk.data.path = [temp_dir.name]

from flask import Flask, render_template, request
from textblob import TextBlob
from newspaper import Article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    polarity = 0  # Initialize polarity to 0
    if request.method == 'POST':
        url = request.form['url']
        article = Article(url)
        try:
            article.download()
            article.parse()
            article.nlp()
            text = article.summary
            obj = TextBlob(text)
            polarity = obj.sentiment.polarity
            print(f"Sentiment Polarity: {polarity}")
            if polarity > 0:
                body_class = 'positive-body'
            else:
                body_class = 'negative-body'
            return render_template('index.html', body_class=body_class, polarity=polarity)
        except Exception as e:
            return render_template('index.html', error=str(e), polarity=polarity)
    return render_template('index.html', polarity=polarity)
