
"""
server.py
This file implements a Flask web server for the Emotion Detection application.
It exposes an endpoint to analyze text and return the detected emotions.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask ('Emotion Detector')

@app.route('/emotionDetector')
def detection_deplyment():

    """
    Flask route handler for the /emotionDetector endpoint.
    """
    emotion_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(emotion_to_analyze)

    if response['dominant_emotion'] is None :
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():

    """
    Flask route handler for the rendering the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
