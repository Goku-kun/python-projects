from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re

list_don = []
better_don = ""
better_ody = ""
with open("Don_Quixote_by_Miguel_De_Cervantes_Saavedra.txt","r", encoding="utf8") as don:
      better_don = re.sub(r"[\W ]", " ", don.read().lower())

with open("The_Odyssey_by_Homer.txt","r", encoding="utf8") as ody:
      better_ody = re.sub(r"[\W ]", " ", ody.read().lower())

test_text = """
and said he to his master  very well then señor i ll hold myself in readiness to gratify your worship s wishes if i m to profit by it  for the love of my wife and children forces me to seem grasping  let your worship say how much you will pay me for each lash i give myself     if sancho   replied don quixote   i were to requite thee as the importance and nature of the cure deserves  the treasures of venice  the mines of potosi  would be insufficient
"""

labels = ["Don", "Homer"]
train_doc = [better_don] + [better_ody]
bow_vectorizer = CountVectorizer()
train_vector = bow_vectorizer.fit_transform(train_doc)
check_vector = bow_vectorizer.transform([test_text])

text_classifier = MultinomialNB()
text_classifier.fit(train_vector, labels)
prediction = text_classifier.predict_proba(check_vector)

print(prediction)