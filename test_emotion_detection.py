from EmotionDetection import emotion_detector

def test_emotion_detection():

    # Test 1 — Joy
    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == 'joy'

    # Test 2 — Anger
    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == 'anger'

    # Test 3 — Disgust
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == 'disgust'

    # Test 4 — Sadness
    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == 'sadness'

    # Test 5 — Fear
    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == 'fear'


# Run tests
test_emotion_detection()

print("All tests passed!")