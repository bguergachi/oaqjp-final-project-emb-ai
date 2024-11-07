
from EmotionDetection.emotion_detection import sentiment_analyzer
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = sentiment_analyzer("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        result = sentiment_analyzer("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = sentiment_analyzer("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        result = sentiment_analyzer("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = sentiment_analyzer("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()

