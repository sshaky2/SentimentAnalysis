import nltk
from flask import Flask, jsonify, request
#from nltk import tokenize, punkt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#nltk.download('punkt')
#nltk.download('vader_lexicon')

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
