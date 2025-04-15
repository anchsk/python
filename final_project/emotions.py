data = {'emotionPredictions':
        [{'emotion':
          {'anger': 0.01364663, 'disgust': 0.0017160787,
           'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024},
            'target': '',
            'emotionMentions':
            [{'span': {'begin': 0, 'end': 27, 'text': 'I love this new technology.'},
              'emotion': {
                'anger': 0.01364663, 'disgust': 0.0017160787, 'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024}}]}], 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}

emotions = data['emotionPredictions'][0]['emotion']
dominant_emotion = max(emotions, key=emotions.get)


res = {
    "anger": 0.006274985,
    "disgust": 0.0025598293,
    "fear": 0.009251528,
    "joy": 0.9680386,
    "sadness": 0.049744144,
    "dominant_emotion": "joy"
}
items = ''

for k, v in res.items():
    if k != 'dominant_emotion':
        items += f"'{k}: {v}, "

items = items.strip()[:-1]
items_2 = ", ".join([f"'{k}': {v}" for k,v in res.items() if k!= 'dominant_emotion'])

print(items_2)

output = 'The sentiment is: {}. The dominant emotion is: {}.'.format(items, res['dominant_emotion'])
print(output)
