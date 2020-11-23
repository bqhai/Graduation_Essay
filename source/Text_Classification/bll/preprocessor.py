import regex as re
from underthesea import word_tokenize

# uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
# unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"


# --Standardized Vietnamese charset--
def load_dict_char():
    dic = {}
    char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
        '|')
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        '|')
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic


dict_char = load_dict_char()


# --Function convert Built-in Unicode to Unicode combinatorial (common)--
def convert_unicode(txt):
    return re.sub(
        r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
        lambda x: dict_char[x.group()], txt)


# --Convert to telex when turn off Unikey--
vowel_table = [['a', 'à', 'á', 'ả', 'ã', 'ạ', 'a'],
               ['ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'aw'],
               ['â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'aa'],
               ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'e'],
               ['ê', 'ề', 'ế', 'ể', 'ễ', 'ệ', 'ee'],
               ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị', 'i'],
               ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'o'],
               ['ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'oo'],
               ['ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ', 'ow'],
               ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'u'],
               ['ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự', 'uw'],
               ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ', 'y']]
first_char = ['', 'f', 's', 'r', 'x', 'j']

vowel_to_ids = {}

for i in range(len(vowel_table)):
    for j in range(len(vowel_table[i]) - 1):
        vowel_to_ids[vowel_table[i][j]] = (i, j)


def standardized_vietnamese_accent_word(word):
    if not is_valid_vietnam_word(word):
        return word
    chars = list(word)
    accent_position = 0
    vowel_index = []
    qu_or_gi = False
    for index, char in enumerate(chars):
        x, y = vowel_to_ids.get(char, (-1, -1))
        if x == -1:
            continue
        elif x == 9:  # check qu
            if index != 0 and chars[index - 1] == 'q':
                chars[index] = 'u'
                qu_or_gi = True
        elif x == 5:  # check gi
            if index != 0 and chars[index - 1] == 'g':
                chars[index] = 'i'
                qu_or_gi = True
        if y != 0:
            accent_position = y
            chars[index] = vowel_table[x][0]
        if not qu_or_gi or index != 1:
            vowel_index.append(index)
    if len(vowel_index) < 2:
        if qu_or_gi:
            if len(chars) == 2:
                x, y = vowel_to_ids.get(chars[1])
                chars[1] = vowel_table[x][accent_position]
            else:
                x, y = vowel_to_ids.get(chars[2], (-1, -1))
                if x != -1:
                    chars[2] = vowel_table[x][accent_position]
                else:
                    chars[1] = vowel_table[5][accent_position] if chars[1] == 'i' else vowel_table[9][accent_position]
            return ''.join(chars)
        return word

    for index in vowel_index:
        x, y = vowel_to_ids[chars[index]]
        if x == 4 or x == 8:  # ê, ơ
            chars[index] = vowel_table[x][accent_position]
            return ''.join(chars)

    if len(vowel_index) == 2:
        if vowel_index[-1] == len(chars) - 1:
            x, y = vowel_to_ids[chars[vowel_index[0]]]
            chars[vowel_index[0]] = vowel_table[x][accent_position]
        else:
            x, y = vowel_to_ids[chars[vowel_index[1]]]
            chars[vowel_index[1]] = vowel_table[x][accent_position]
    else:
        x, y = vowel_to_ids[chars[vowel_index[1]]]
        chars[vowel_index[1]] = vowel_table[x][accent_position]
    return ''.join(chars)


def is_valid_vietnam_word(word):
    chars = list(word)
    vowel_index = -1
    for index, char in enumerate(chars):
        x, y = vowel_to_ids.get(char, (-1, -1))
        if x != -1:
            if vowel_index == -1:
                vowel_index = index
            else:
                if index - vowel_index != 1:
                    return False
                vowel_index = index
    return True


def standardized_vietnamese_accent_sentence(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    for index, word in enumerate(words):
        cw = re.sub(r'(^\p{P}*)([p{L}.]*\p{L}+)(\p{P}*$)', r'\1/\2/\3', word).split('/')
        # print(cw)
        if len(cw) == 3:
            cw[1] = standardized_vietnamese_accent_word(cw[1])
        words[index] = ''.join(cw)
    return ' '.join(words)


def remove_html(txt):
    return re.sub(r'<[^>]*>', '', txt)


def text_preprocess(document):
    # remove html code
    document = remove_html(document)
    # standardized unicode
    document = convert_unicode(document)
    # standardized typing Vietnamese accents
    document = standardized_vietnamese_accent_sentence(document)
    # word tokenize
    document = word_tokenize(document, format="text")
    # convert to lower
    document = document.lower()
    # remove unnecessary char
    document = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]', ' ', document)
    # remove unnecessary white space
    document = re.sub(r'\s+', ' ', document).strip()
    return document
