my_dict = {
    "response": {
        "results": {
            "alternatives": {
                "transcript": "Recognised text from your speech"
            },

            "alternatives2": {
                "transcript": "Recognised text from your speech"
            }
        }
    }
}
text = my_dict.get("response").get('results').get('alternatives') # or .pop('alternatives')
print(text)
