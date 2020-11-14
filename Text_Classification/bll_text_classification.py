import os
import pickle

from preprocessor import text_preprocess
from train_model import label_encoder

MODEL_PATH = "models"
text = []
label = []

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
