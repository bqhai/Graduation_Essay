__author__ = 'Hai Bui'

total_label = 14
vocab = {}
label_vocab = {}
count = {}
# Count by label
for line in open('../data/news_categories_v5.txt', encoding='utf8'):
    key = line.split()[0]
    count[key] = count.get(key, 0) + 1

for key in count:
    print(key, count[key])

for line in open('../data/news_categories_v5.txt', encoding='utf8'):
    words = line.split()
    # first word is label
    label = words[0]
    if label not in label_vocab:
        label_vocab[label] = {}
    for word in words[1:]:
        label_vocab[label][word] = label_vocab[label].get(word, 0) + 1
        if word not in vocab:
            vocab[word] = set()
        vocab[word].add(label)

count = {}
for word in vocab:
    if len(vocab[word]) == total_label:
        count[word] = min([label_vocab[x][word] for x in label_vocab])

sorted_count = sorted(count, key=count.get, reverse=True)
for word in sorted_count[:100]:
    print(word, count[word])

# Save stopword to file
stopword = set()
with open('../data/stopwords.txt', 'w', encoding='utf8') as fp:
    for word in sorted_count[:100]:
        stopword.add(word)
        fp.write(word + '\n')


# Remove stopword
def remove_stopwords(line):
    words = []
    for word in line.strip().split():
        if word not in stopword:
            words.append(word)
    return ' '.join(words)


with open('../data/news_categories_v5.prep', 'w', encoding='utf8') as fp:
    for line in open('../data/news_categories_v5.txt', encoding='utf8'):
        line = remove_stopwords(line)
        fp.write(line + '\n')
