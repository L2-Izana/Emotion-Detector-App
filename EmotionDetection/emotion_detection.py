import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    full_analyzed_result_str = requests.post(url, headers=headers, json=input_json).text
    analyzed_result_json = json.loads(full_analyzed_result_str)
    analyzed_emotion_result_json = analyzed_result_json.get('emotionPredictions')[0].get('emotion')
    anger_score = analyzed_emotion_result_json.get('anger')
    disgust_score = analyzed_emotion_result_json.get('disgust')
    fear_score = analyzed_emotion_result_json.get('fear')
    joy_score = analyzed_emotion_result_json.get('joy')
    sadness_score = analyzed_emotion_result_json.get('sadness')
    emotions_metric_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = ''
    dominant_emotion_metric = 0
    for emotion in emotions_metric_output:
        if emotions_metric_output[emotion] > dominant_emotion_metric:
            dominant_emotion = emotion
            dominant_emotion_metric = emotions_metric_output[emotion]
    emotions_metric_output['dominant_emotion'] = dominant_emotion
    return emotions_metric_output