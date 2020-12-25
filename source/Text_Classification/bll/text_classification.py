__author__ = 'Hai Bui'
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from sklearn import pipeline, naive_bayes, calibration
from bll.preprocessor import text_preprocess


test_percent = 0.2
text = []
label = []

# load label
for line in open('data/news_categories_v4.prep', encoding='utf8'):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)

# encode label
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

nb_model = pickle.load(open('models/naive_bayes_v4.pkl', 'rb'))
# linear_model = pickle.load(open(os.path.join(c.MODEL_PATH, 'linear_classifier.pkl'), 'rb'))


def predict(input_data):
    clean_text = text_preprocess(input_data)
    text_label = nb_model.predict([clean_text])
    return label_encoder.inverse_transform(text_label)
# def predict(input_data):
#     clean_text = text_preprocess(input_data)
#     text_label = linear_model.predict([clean_text])
#     return label_encoder.inverse_transform(text_label)


def convert_label_to_text(label):
    if Counter(label) == Counter(['__label__công_nghệ']):
        return ['CN', 'CÔNG NGHỆ', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__thể_thao']):
        return ['TTH', 'THỂ THAO', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__âm_nhạc']):
        return ['AN', 'ÂM NHẠC', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__thời_sự']):
        return ['TS', 'THỜI SỰ', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__thời_trang']):
        return ['TTR', 'THỜI TRANG', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__giáo_dục']):
        return ['GD', 'GIÁO DỤC', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__kinh_doanh']):
        return ['KD', 'KINH DOANH', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__phim_ảnh']):
        return ['PA', 'PHIM ẢNH', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__xe']):
        return ['XE', 'XE', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__ẩm_thực']):
        return ['AT', 'ẨM THỰC', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__sức_khỏe']):
        return ['SK', 'SỨC KHỎE', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__an_ninh_trật_tự']):
        return ['ANTT', 'AN NINH TRẬT TỰ', 'NEU', 'BÌNH THƯỜNG']
    elif Counter(label) == Counter(['__label__an_ninh_quốc_gia_neg']):
        return ['ANQG', 'AN NINH QUỐC GIA', 'NEG', 'TIÊU CỰC']
    elif Counter(label) == Counter(['__label__an_ninh_quốc_gia_pos']):
        return ['ANQG', 'AN NINH QUỐC GIA', 'POS', 'TÍCH CỰC']
