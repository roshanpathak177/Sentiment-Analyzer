# Sentiment Analyzer

A simple web application built with Flask that analyzes the sentiment of articles or web pages by extracting the text and calculating the polarity score using TextBlob and NLTK.

![Sentiment Analyzer Demo](https://i.imgur.com/XYVGndO.png)

## Features

- Enter the URL of any web article or page
- Extracts the text content using `newspaper3k`
- Calculates the sentiment polarity score using TextBlob and NLTK
- Displays the polarity score and categorizes it as extremely positive/negative, very positive/negative, positive/negative, moderately positive/negative, slightly positive/negative, or neutral
- Responsive design with a clean and modern user interface

## Getting Started

To get started with the Sentiment Analyzer, simply visit [https://sentiment-analyzer-psi-one.vercel.app/](https://sentiment-analyzer-psi-one.vercel.app/).

## Usage

1. Open your web browser and visit [https://sentiment-analyzer-psi-one.vercel.app/](https://sentiment-analyzer-psi-one.vercel.app/)

2. Enter the URL of the article or web page you want to analyze

3. Click the "Analyze" button

4. The sentiment polarity score will be displayed, along with its classification

## Deployment

This project is deployed on Vercel and can be accessed at [https://sentiment-analyzer-psi-one.vercel.app/](https://sentiment-analyzer-psi-one.vercel.app/).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [TextBlob](https://textblob.readthedocs.io/en/dev/) - For sentiment analysis
- [NLTK](https://www.nltk.org/) - Natural Language Toolkit for text processing
- [newspaper3k](https://newspaper.readthedocs.io/en/latest/) - For extracting article text from URLs
