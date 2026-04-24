# Import unittest framework for running test cases
import unittest

# Import the emotion_detector function from the EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector


# Create a test class that inherits from unittest.TestCase
class TestEmotionDetector(unittest.TestCase):
    """Unit tests for emotion detection."""

    # Test case to verify joy detection
    def test_joy(self):
        # Call the function with a joyful statement
        result = emotion_detector("I am glad this happened")
        # Check if dominant emotion returned is 'joy'
        self.assertEqual(result['dominant_emotion'], 'joy')

    # Test case to verify anger detection
    def test_anger(self):
        # Call the function with an angry statement
        result = emotion_detector("I am really mad about this")
        # Check if dominant emotion returned is 'anger'
        self.assertEqual(result['dominant_emotion'], 'anger')

    # Test case to verify disgust detection
    def test_disgust(self):
        # Call the function with a disgust-related statement
        result = emotion_detector("I feel disgusted just hearing about this")
        # Check if dominant emotion returned is 'disgust'
        self.assertEqual(result['dominant_emotion'], 'disgust')

    # Test case to verify sadness detection
    def test_sadness(self):
        # Call the function with a sad statement
        result = emotion_detector("I am so sad about this")
        # Check if dominant emotion returned is 'sadness'
        self.assertEqual(result['dominant_emotion'], 'sadness')

    # Test case to verify fear detection
    def test_fear(self):
        # Call the function with a fear-related statement
        result = emotion_detector("I am really afraid that this will happen")
        # Check if dominant emotion returned is 'fear'
        self.assertEqual(result['dominant_emotion'], 'fear')


# Main block to execute the unit tests
if __name__ == "__main__":
    # Run all test cases
    result = unittest.main(exit=False)

    # Print message only if all tests pass successfully
    if result.result.wasSuccessful():
        print("All test cases passed!")