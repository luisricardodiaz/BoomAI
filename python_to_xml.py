from emotion_detection import emotion_from_string
from speech_capture import recording_input


def create_xml(response: str):
    style = emotion_from_string(response)
    #print(type(style))

    dict = {"Admiration":"cheerful",
    "Adoration":"friendly",
    "Aesthetic Appreciation":"cheerful",
    "Amusement":"cheerful",
    "Anger":"unfriendly",
    "Annoyance":"unfriendly",
    "Anxiety":"sad",
    "Awe":"hopeful",
    "Awkwardness":"whispering",
    "Boredom":"customerservice",
    "Calmness":"narration-professional",
    "Concentration":"chat",
    "Confusion":"terrified",
    "Contemplation":"sad",
    "Contempt":"sad",
    "Contentment":"hopeful",
    "Craving":"hopeful",
    "Determination":"hopeful",
    "Disappointment":"unfriendly",
    "Disapproval":"unfriendly",
    "Disgust":"unfriendly",
    "Distress":"shouting",
    "Doubt":"whispering",
    "Ecstasy":"excited",
    "Embarrassment":"whispering",
    "Empathic Pain":"shouting",
    "Enthusiasm":"cheerful",
    "Entrancement": "newcast-casual",
    "Envy": "terrified",
    "Excitement":"excited",
    "Fear":"terified",
    "Gratitude": "friendly",
    "Guilt":"sad",
    "Horror":"terrified",
    "Interest": "cheerful",
    "Joy": "cheerful",
    "Love": "hopeful",
    "Nostalgia": "sad",
    "Pain": "sad",
    "Pride": "hopeful",
    "Realization": "narration-professional",
    "Relief": "friendly",
    "Romance": "friendly",
    "Sadness": "sad",
    "Sarcasm": "friendly",
    "Satisfaction": "excited",
    "Desire": "hopeful",
    "Shame": "sad",
    "Surprise (negative)": "unfriendly",
    "Surprise (positive)":"excited",
    "Sympathy":"empathetic",
    "Tiredness": "whispering",
    "Triumph": "shouting"}

    header = f"<speak version=\"1.0\" xmlns=\"https://www.w3.org/2001/10/synthesis\"  xmlns:mstts=\"https://www.w3.org/2001/mstts\" xml:lang=\"en-US\">\n\
    \t\t<voice name=\"en-US-AriaNeural\">\n\
    \t\t\t\t<mstts:express-as style=\"{dict[str(style)]}\" styledegree=\"2\">\n"
    text = f"\t\t\t\t\t\t{response}\n"
    footer = f"\t\t\t\t</mstts:express-as>\n\
    \t\t</voice>\n\
    </speak>"

    f = open("output.xml", "w")
    f.write(header + text + footer)
    f.close()


