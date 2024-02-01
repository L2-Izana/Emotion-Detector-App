from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def emotionDetector():
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def get_emotion_report():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_analyzed_result = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is 'anger': {emotion_analyzed_result.get('anger')}, 'disgust': {emotion_analyzed_result.get('disgust')}. 'fear':{emotion_analyzed_result.get('fear')}, 'joy':{emotion_analyzed_result.get('joy')} and 'sadness':{emotion_analyzed_result.get('sadness')}. The dominant emotion is {emotion_analyzed_result.get('dominant_emotion')}."

if __name__ == '__main__':
    app.run(debug=True)