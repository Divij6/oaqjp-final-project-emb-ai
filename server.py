"""
Flask server for Emotion Detection application.
Handles routing and returns detected emotions in JSON format.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Root route to verify server is running.

    Returns:
        dict: Simple status message.
    """
    return jsonify({"message": "Emotion Detection Server Running"})


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to detect emotions from user input text.

    Returns:
        JSON response containing emotion scores
        or error message if input is invalid.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detector
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    # Handle blank input
    if dominant_emotion is None:
        return jsonify({'error': 'Invalid text! Please try again!'})

    return jsonify({
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness'],
        'dominant_emotion': dominant_emotion
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
