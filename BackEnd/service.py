import spacy
import pandas as pd
import random

nlp = spacy.load("fr_core_news_lg")
data = pd.read_csv("data.csv")

subjects = {
    1: "JavaScript",
    2: "HTML",
    3: "CSS",
    4: "Python niveau 1",
    5: "PL/SQL",
    6: "Python (POO)",
    7: "Java (POO)",
    8: "Base de données",
    9: "IA",
    10: "ML",
    11: "DL"
}


def getShuffeledQuestions(subjectId):
    subjectId = int(subjectId)
    subject = subjects.get(subjectId)
    filtered_questions = data[data["Domaine"] == subject]["Question"].tolist()
    random.shuffle(filtered_questions)
    return filtered_questions[:5]


def calculateScore(document):
    question = next(iter(document.keys()))
    answer = document[question]
    correctAnswer = data[data['Question']==question].iloc[0][2]
    s1 = nlp(correctAnswer)
    s2 = nlp(answer)
    s1verbs = " ".join([token.lemma_ for token in s1 if token.pos_ == "VERB"])
    s1ajds = " ".join([token.lemma_ for token in s1 if token.pos_ == "ADJ"])
    s1nous = " ".join([token.lemma_ for token in s1 if token.pos_ == "NOUN"])
    s2verbs = " ".join([token.lemma_ for token in s2 if token.pos_ == "VERB"])
    s2ajds = " ".join([token.lemma_ for token in s2 if token.pos_ == "ADJ"])
    s2nous = " ".join([token.lemma_ for token in s2 if token.pos_ == "NOUN"])
    resultverbs = nlp(s1verbs).similarity(nlp(s2verbs))
    resultajds = nlp(s1ajds).similarity(nlp(s2ajds))
    resultnoun = nlp(s1nous).similarity(nlp(s2nous))
    return s1.similarity(s2),resultverbs,resultajds,resultnoun,correctAnswer
