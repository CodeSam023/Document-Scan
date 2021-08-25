import pickle
from script.clean_data import text_preprocessing

def get_classified_lines(lines):
    clean_lines = []
    for i in lines:
        clean_line = text_preprocessing(i)
        clean_lines.append(clean_line)
    vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))
    vectorized_texts = vectorizer.transform(clean_lines)
    RFC =  pickle.load(open("model/Random_Forest_Classifier.pkl", "rb"))
    predictions = RFC.predict(vectorized_texts) 
    data = {"positive":[], "negative":[]}
    for i,line in enumerate(lines):
        if predictions[i] == 0:
            if len(line.split(" ")) > 5:
                data["positive"].append(line)
        else:
            if len(line.split(" ")) > 5:
                data["negative"].append(line)
    return data