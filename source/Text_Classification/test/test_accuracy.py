__author__ = 'Hai Bui'

from sklearn.metrics import classification_report
import pickle
import os
import bll.common as c
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
test_percent = 0.2
text = []
label = []
if not os.path.exists(c.MODEL_PATH):
    os.makedirs(c.MODEL_PATH)
for line in open('../data/news_categories_v2.prep', encoding='utf8'):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)

# encode label
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

nb_model = pickle.load(open(os.path.join(c.MODEL_PATH, 'naive_bayes_v2.pkl'), 'rb'))
y_pred = nb_model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=list(label_encoder.classes_)))
