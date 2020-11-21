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

input_data2 = ["""📣📣 𝐌𝐚̣𝐧𝐡 𝐡𝐨̛𝐧 𝐢𝟕 - 𝐆𝐢𝐚́ 𝐜𝐡𝐢̉ 𝐢𝟑 📣📣
😲 Chỉ chưa tới 𝟏𝟎 𝐭𝐫𝐢𝐞̣̂𝐮 - sở hữu ngay bộ máy mạnh hơn 𝐢𝟕 𝟕𝐭𝐡 😲
🖥 Cấu hình phá đảo:
💪 CPU 𝐈𝐧𝐭𝐞𝐥 𝐂𝐨𝐫𝐞 𝐢𝟑-𝟏𝟎𝟏𝟎𝟎𝐅 4 nhân 8 luồng mạnh mẽ
💪 RAM 𝟖𝐆𝐁 𝐃𝐃𝐑𝟒 𝐁𝐮𝐬 𝟐𝟔𝟔𝟔 xịn sò
💪 VGA 𝐆𝐢𝐠𝐚𝐛𝐲𝐭𝐞 𝐆𝐓𝐗 𝟏𝟔𝟓𝟎 𝐃𝐃𝐑𝟔 𝟒𝐆𝐁 gaming hoàn hảo
🚀 Các gói ưu đãi siêu khủng:
🔥 Nâng cấp lên 𝐑𝐀𝐌 𝟏𝟔𝐆𝐁 miễn phí.
🔥 Combo 𝐁𝐚̀𝐧 𝐩𝐡𝐢́𝐦 𝐜𝐨̛ + 𝐂𝐡𝐮𝐨̣̂𝐭 𝐆𝐚𝐦𝐢𝐧𝐠 + 𝐋𝐨́𝐭 𝐜𝐡𝐮𝐨̣̂𝐭 ̣.
🔥 Voucher 𝟓𝟎𝟎𝐤.""",
"""Livestream Trao giải Vòng loại Đấu sĩ Coder 2020 ngày 16/11/2020
Bốc thăm chia bảng Tứ Kết AI Game ngày 19/11""",
"""Học lén người ta bí quyết lên Hội Chủ Shop GrabExpress bán hàng thì cũng phải biết chọn đúng đồ để bán chứ. Ghét tối cho ra sofa ngủ, Lèo vô phòng ngủ với Mén."""]

for item in input_data2:
    print(predict(item))







