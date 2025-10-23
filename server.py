"""Flask app exposing an endpoint for Watson-based emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """HTTP GET endpoint `/emotionDetector` that returns detected emotions for the given text."""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    response_text = (
    f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}.")
    return response_text
@app.route("/")
def render_index_page():
    """Render the landing page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
