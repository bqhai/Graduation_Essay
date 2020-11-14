import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from preprocessor import text_preprocess

MODEL_PATH = "models"
test_percent = 0.2
text = []
label = []

# load label
if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
for line in open('data/news_categories.prep', encoding="utf8"):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)

# encode label
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

# Naive Bayes
# model = pickle.load(open(os.path.join(MODEL_PATH,"naive_bayes.pkl"), 'rb'))
# y_pred = model.predict(X_test)
# print('Naive Bayes, Accuracy =', np.mean(y_pred == y_test))
#
# Print result all label
# y_pred = nb_model.predict(X_test)
# print(classification_report(y_test, y_pred, target_names=list(label_encoder.classes_)))


nb_model = pickle.load(open(os.path.join(MODEL_PATH, "naive_bayes.pkl"), 'rb'))


def predict(input_data):
    text = text_preprocess(input_data)
    label = nb_model.predict([text])
    return label_encoder.inverse_transform(label)
