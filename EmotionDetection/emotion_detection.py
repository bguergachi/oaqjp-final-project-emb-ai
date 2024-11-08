import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Initialize emotions dictionary with None values
    emotions = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions.update(formatted_response["emotionPredictions"][0]["emotion"])

        # Filter out None values to ensure max() only works with valid numbers
        valid_emotions = {emotion: score for emotion, score in emotions.items() if score is not None}
        
        if valid_emotions:
            # Find the highest score from valid emotions
            highest_emotion = max(valid_emotions, key=valid_emotions.get)
            emotions["dominant_emotion"] = highest_emotion
        else:
            emotions["dominant_emotion"] = None  

    elif response.status_code == 400:
        return emotions
    
    return emotions
