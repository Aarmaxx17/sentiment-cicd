from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):

    scores = analyzer.polarity_scores(text)

    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"

    elif compound <= -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    confidence = round(abs(compound) * 100, 2)

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "scores": scores
    }


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    text = ""

    if request.method == "POST":

        text = request.form.get("text", "")

        if text.strip():
            result = analyze_sentiment(text)

    return render_template(
        "index.html",
        result=result,
        text=text
    )


@app.route("/api/analyze", methods=["POST"])
def api_analyze():

    data = request.get_json()

    if not data or not data.get("text"):

        return jsonify({
            "error": "Text is required"
        }), 400

    return jsonify(
        analyze_sentiment(data["text"])
    )


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "service": "sentiment-analysis"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
