import nltk
from flask import Flask, jsonify, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('punkt')
nltk.download('vader_lexicon')

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def get_score():
    text = request.data.decode(encoding='UTF-8')
    if (not text):
        return '<h1>In order to calculate the sentiment score, you need to HTTP POST the body with raw text to this address.</h1><br> \
        Score is returned in form of JSON object. Compound score is the average score which ranges from -1 to +1. -1 being most negative and \
        +1 being most positive.'
    else:
        sid = SentimentIntensityAnalyzer()
        return jsonify(sid.polarity_scores(request.data.decode(encoding='UTF-8')))


if __name__ == '__main__':
    app.run(debug=True)
