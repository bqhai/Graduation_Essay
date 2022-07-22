__author__ = 'Hai Bui'

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import bll.common as c
import os
import pickle
import time

test_percent = 0.2
text = []
label = []
if not os.path.exists(c.MODEL_PATH):
    os.makedirs(c.MODEL_PATH)

for line in open('../data/news_categories_v5.prep', encoding='utf8'):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)

# encode label
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

# --Train Linear Classifier--
start_time = time.time()
text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1, 1),
                                              max_df=0.8,
                                              max_features=None)),
                     ('tfidf', TfidfTransformer()),
                     ('clf', LogisticRegression(solver='lbfgs',
                                                multi_class='auto',
                                                max_iter=10000))
                     ])
text_clf = text_clf.fit(X_train, y_train)

train_time = time.time() - start_time
print('Done training Linear Classifier in', train_time, 'seconds.')

# Save model
pickle.dump(text_clf, open(os.path.join(c.MODEL_PATH, 'linear_classifier_v5.pkl'), 'wb'))
