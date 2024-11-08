import requests  # Import the requests library to handle HTTP requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    # Find the highest score 
    highest_emotion = max(emotions, key=emotions.get) 
    emotions["dominant_emotion"] = highest_emotion
    return emotions

