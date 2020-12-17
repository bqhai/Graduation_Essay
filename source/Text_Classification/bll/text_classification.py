__author__ = 'Hai Bui'
import os
import pickle
import bll.common as c
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from bll.preprocessor import text_preprocess


test_percent = 0.2
text = []
label = []

# load label
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
        return 'CÔNG NGHỆ'
    elif Counter(label) == Counter(['__label__thể_thao']):
        return 'THỂ THAO'
    elif Counter(label) == Counter(['__label__âm_nhạc']):
        return 'ÂM NHẠC'
    elif Counter(label) == Counter(['__label__thời_sự']):
        return 'THỜI SỰ'
    elif Counter(label) == Counter(['__label__thời_trang']):
        return 'THỜI TRANG'
    elif Counter(label) == Counter(['__label__du_lịch']):
        return 'DU LỊCH'
    elif Counter(label) == Counter(['__label__giáo_dục']):
        return 'GIÁO DỤC'
    elif Counter(label) == Counter(['__label__kinh_doanh']):
        return 'KINH DOANH'
    elif Counter(label) == Counter(['__label__an_ninh_trật_tự']):
        return 'AN NINH TRẬT TỰ'
    elif Counter(label) == Counter(['__label__phim_ảnh']):
        return 'PHIM ẢNH'
    elif Counter(label) == Counter(['__label__xe_360']):
        return 'XE'
    elif Counter(label) == Counter(['__label__ẩm_thực']):
        return 'ẨM THỰC'
    elif Counter(label) == Counter(['__label__xuất_bản']):
        return 'XUẤT BẢN'
    elif Counter(label) == Counter(['__label__sức_khỏe']):
        return 'SỨC KHỎE'
    elif Counter(label) == Counter(['__label__thế_giới']):
        return 'THẾ GIỚI'
    elif Counter(label) == Counter(['__label__chính_trị']):
        return 'CHÍNH TRỊ'


def convert_label_to_labelID(label):
    if Counter(label) == Counter(['__label__công_nghệ']):
        return 'CN'
    elif Counter(label) == Counter(['__label__thể_thao']):
        return 'TTH'
    elif Counter(label) == Counter(['__label__âm_nhạc']):
        return 'AN'
    elif Counter(label) == Counter(['__label__thời_sự']):
        return 'TS'
    elif Counter(label) == Counter(['__label__thời_trang']):
        return 'TTR'
    elif Counter(label) == Counter(['__label__du_lịch']):
        return 'DL'
    elif Counter(label) == Counter(['__label__giáo_dục']):
        return 'GD'
    elif Counter(label) == Counter(['__label__kinh_doanh']):
        return 'KD'
    elif Counter(label) == Counter(['__label__an_ninh_trật_tự']):
        return 'ANTT'
    elif Counter(label) == Counter(['__label__phim_ảnh']):
        return 'PA'
    elif Counter(label) == Counter(['__label__xe_360']):
        return 'XE'
    elif Counter(label) == Counter(['__label__ẩm_thực']):
        return 'AT'
    elif Counter(label) == Counter(['__label__xuất_bản']):
        return 'XB'
    elif Counter(label) == Counter(['__label__sức_khỏe']):
        return 'SK'
    elif Counter(label) == Counter(['__label__thế_giới']):
        return 'TG'
    elif Counter(label) == Counter(['__label__chính_trị']):
        return 'CT'

# input_data2 = '''THEO BẠN BÊN NÀO LÀ NỤ CƯỜI ĐANG GIẢ TẠO? 😃
# ----------------------------------------
# Làm thế nào để chúng ta biết được nụ cười đó có chân thật hay không, khi mà có rất nhiều nụ cười giả tạo của người đối diện khiến ta hiểu sai tình huống? Bài viết dưới đây sẽ giúp bạn giải quyết vấn đề này:
# Nụ cười là ngôn ngữ chung trên thế giới đại diện cho sự thân thiện. Nhưng làm thế nào để chúng ta biết được nụ cười đó có chân thật hay không?
# Nhà tâm lí học Richard Wiseman đã tiến hành một cuộc nghiên cứu để chứng minh khả năng nhận biết độ “thật” của nụ cười của con người.
# Nhiếp ảnh gia sẽ yêu cầu người được chụp tưởng tượng đang gặp một người mà họ không ưa và sau đó nở nụ cười giải tạo; tiếp theo họ sẽ tưởng tượng họ đang gặp một người bạn thân và nở một nụ cười chân thành. Tất nhiên, cả hai tình huống trên sẽ được nhiếp ảnh gia chụp lại.
# Câu hỏi đặt ra là nhận biết nụ cười “giả” và “thật” có khó không? “Nếu bạn không có sự đồng cảm, bạn sẽ khó mà phân biệt được sự khác biệt giữa hai bức ảnh“, Wiseman cho biết.
# Qua khảo sát ông cho biết khoảng 60% người bình thường sẽ phân biệt được sự khác nhau trên, trong khi những người hay đi tiệc tùng sẽ chiếm tỉ lệ cao hơn: 66%.
# Ngoài ra các phóng viên và nhà khoa học xã hội là những người có tỉ lệ đoán đúng cao nhất: 73% và 80% lần lượt. Hay nói cách khác, những người làm công việc có liên quan đến con người hay tiếp xúc nhiều với con người sẽ nhận định được sự khác nhau giữa nụ cười “giả” và “thật” dễ dàng hơn.
# ____________'''
#
#
# def predict2(input_data):
#     clean_text = text_preprocess(input_data)
#     text_label = nb_model.predict([clean_text])
#     return text_label
# print(predict2(input_data2))

# Naive Bayes
# model = pickle.load(open(os.path.join(MODEL_PATH,"naive_bayes.pkl"), 'rb'))
# y_pred = model.predict(X_test)
# print('Naive Bayes, Accuracy =', np.mean(y_pred == y_test))
#
# Print result all label
# y_pred = nb_model.predict(X_test)
# print(classification_report(y_test, y_pred, target_names=list(label_encoder.classes_)))
