__author__ = 'Hai Bui'
import os
import pickle
import bll.common as c
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from bll.preprocessor import text_preprocess


# test_percent = 0.2
# text = []
# label = []
#
# # load label
# if not os.path.exists(c.MODEL_PATH):
#     os.makedirs(c.MODEL_PATH)
# for line in open('../data/news_categories_v3.prep', encoding='utf8'):
#     words = line.strip().split()
#     label.append(words[0])
#     text.append(' '.join(words[1:]))
#
# X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)
#
# # encode label
# label_encoder = LabelEncoder()
# label_encoder.fit(y_train)
# y_train = label_encoder.transform(y_train)
# y_test = label_encoder.transform(y_test)

nb_model = pickle.load(open(os.path.join(c.MODEL_PATH, 'naive_bayes_v2.pkl'), 'rb'))
# linear_model = pickle.load(open(os.path.join(c.MODEL_PATH, 'linear_classifier.pkl'), 'rb'))


def predict(input_data):
    clean_text = text_preprocess(input_data)
    text_label = nb_model.predict([clean_text])
    return text_label

x = predict('''
món này ngon thế
''')
print(x)