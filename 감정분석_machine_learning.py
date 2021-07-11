from sklearn.model_selection import train_test_split
from tensorflow.keras import metrics
from tensorflow.keras import losses
from tensorflow.keras import optimizers
from tensorflow.keras import layers
from tensorflow.keras import models
import numpy as np
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import os
import json
from konlpy.tag import Okt
import pymysql.cursors
import pandas as pd
import re

# conn = pymysql.connect(host='localhost',
#                        user='lyunj',
#                        password='Dldbswo77@',
#                        db='coupang_review',  # coupang_review 스키마 생성 필요
#                        charset='utf8',
#                        cursorclass=pymysql.cursors.DictCursor)

# try:
#     with conn.cursor() as curs:
#         sql = 'select rating,review_content from csv_save where (rating =1 or rating=5) and review_len <> 0'
#         curs.execute(sql)
#         result = curs.fetchall()
#         df = pd.DataFrame(result)
# finally:
#     conn.close()


# okt = Okt()


# def tokenize(review):
#     return ['/'.join(t) for t in okt.pos(review, norm=True, stem=True)]


# reviews = []
# print(df.loc[1:5])
# for i in df.index:
#     if i % 100 == 0:
#         print('진행개수 : ', i)
#     row = df._get_value(i, 'review_content')
#     row = re.sub('\n', '', row)
#     row = re.sub('\u200b', '', row)
#     row = re.sub('\xa0', '', row)
#     row = re.sub('([a-zA-Z])', '', row)
#     row = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', row)
#     row = re.sub(
#         '[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', row)
#     reviews.append([tokenize(row), str(df._get_value(i, 'rating'))])

# with open('review_token.json', 'w', encoding='utf-8') as make_file:
#     json.dump(reviews, make_file, ensure_ascii=False, indent='\t')


import nltk

with open('review_token.json', encoding='utf-8') as f:
    review_token = json.load(f)

tokens = [t for d in review_token for t in d[0] if (
    t.split('/')[1] == 'Noun') or (t.split('/')[1] == 'Adjective')]

text = nltk.Text(tokens, name='NMSC')

print(len(set(text.tokens)))

# tokens_1 = [t for d in review_token for t in d[0] if (
#     t.split('/')[1] == 'Noun') and len(t.split('/')[0]) > 1 and d[1] == '1']

# text = nltk.Text(tokens_1, name='NMSC')

# rating_1 = text.vocab().most_common(100)

# tokens_5 = [t for d in review_token for t in d[0] if (
#     t.split('/')[1] == 'Noun') and len(t.split('/')[0]) > 1 and d[1] == '5']
# text = nltk.Text(tokens_5, name='NMSC')

# rating_5 = text.vocab().most_common(100)

# rating_1_word = [x[0] for x in rating_1]
# rating_5_word = [x[0] for x in rating_5]

# result = [x for x in rating_5_word if x in rating_1_word]


# tokens_1 = [x for x in tokens_1 if x not in result]

# rating_1 = [x for x in rating_1 if x[0] not in result]
# print(rating_1)

# font_fname = 'c:/windows/fonts/gulim.ttc'
# font_name = font_manager.FontProperties(fname=font_fname).get_name()
# rc('font', family=font_name)

# plt.figure(figsize=(20, 10))
# nltk.Text(tokens_1).plot(100)


selected_words = [f[0] for f in text.vocab().most_common(1000)]


def term_frequency(doc):
    return [doc.count(word) for word in selected_words]


X = [term_frequency(d) for d, _ in review_token]
y = [d for _, d in review_token]
print(y[1:100])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=True, random_state=1004)

x_train = np.asarray(X_train).astype('float32')
x_test = np.asarray(X_test).astype('float32')

y_train = np.asarray(y_train).astype('float32')
y_test = np.asarray(y_test).astype('float32')

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(1000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
              loss=losses.binary_crossentropy,
              metrics=[metrics.binary_accuracy])

model.fit(x_train, y_train, epochs=100, batch_size=64)
results = model.evaluate(x_test, y_test)
print(results)
model.save('saved_model/first_model')
