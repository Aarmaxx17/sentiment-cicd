import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app import app, analyze_sentiment


def test_home():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health():

    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200


def test_positive():

    result = analyze_sentiment(
        "I absolutely love this amazing product"
    )

    assert result["sentiment"] == "Positive"


def test_negative():

    result = analyze_sentiment(
        "This is absolutely terrible and horrible"
    )

    assert result["sentiment"] == "Negative"


def test_neutral():

    result = analyze_sentiment(
        "The book is on the table"
    )

    assert result["sentiment"] == "Neutral"
