import nltk
from flask import Flask, jsonify, request
#from nltk import tokenize, punkt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('punkt')
nltk.download('vader_lexicon')

app = Flask(__name__)


@app.route("/sentiment", methods=['POST'])
def get_score():
    sid = SentimentIntensityAnalyzer()
    return jsonify(sid.polarity_scores(request.data.decode(encoding='UTF-8')))


if __name__ == '__main__':
    app.run(debug=True)
