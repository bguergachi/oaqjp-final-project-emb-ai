from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    # Construct the formatted response string
    formatted_response = (
        f"For the given statement, the system response is:\n"
        f"'anger': {response['anger']},\n"
        f"'disgust': {response['disgust']},\n"
        f"'fear': {response['fear']},\n"
        f"'joy': {response['joy']},\n"
        f"'sadness': {response['sadness']}.\n"
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    # Return the formatted string
    return formatted_response




@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)