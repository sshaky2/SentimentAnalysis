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
        return '<h1>In order to calculate the sentiment score, you need to HTTP POST with text in body to this address.</h1>'
    else:
        sid = SentimentIntensityAnalyzer()
        return jsonify(sid.polarity_scores(request.data.decode(encoding='UTF-8')))


if __name__ == '__main__':
    app.run(debug=True)
