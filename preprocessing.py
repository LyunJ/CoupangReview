import json
import pandas as pd
import numpy as np
import re
import os


def preprocessing_df(df):
    df["newline_count"] = 0
    df["review_len"] = 0
    df["special_char_count"] = 0
    df["manufacturer_count"] = 0
    df["product_count"] = 0

    for i in range(len(df)):
        df["name"][i] = df["name"][i].strip()  # 이름 좌우 공백 제거
        df["text"][i] = df["text"][i].strip()  # 리뷰 좌우 공백 제거
        df["newline_count"][i] = df["text"][i].count(
            '\n')  # 리뷰 중간 개행문자 개수 column 추가
        df["review_len"][i] = len(df["text"][i])  # 리뷰 길이 column 추가
        # , . 을 제외한 나머지 특수문자 count를 위해 모두 %로 변경
        temp_str = re.sub(
            '[-=+#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》⭐️⭕️]', '%', df["text"][i])
        df["special_char_count"][i] = temp_str.count('%')  # 특수 문자 개수 column 추가
        df["manufacturer_count"][i] = df["text"][i].count(
            df["manufacturer"][i])  # 제조사 언급 횟수 column 추가
        df["product_count"][i] = df["text"][i].count(
            df["product"][i])  # 제품명 언급 횟수 column 추가


# cat_list = ['패션의류잡화', '뷰티', '출산유아동', '식품', '주방용품', '생활용품', '홈인테리어',
#            '가전디지털', '스포츠레저', '자동차용품', '도서음반DVD', '완구취미', '문구오피스', '반려동물용품', '헬스건강식품']

cat_list = ['11stReview']

for i in cat_list:
    path = './json_data/' + i
    file_list = os.listdir(path)
    df_list = []
    for j in file_list:
        with open(path + '/' + j, encoding="utf=8") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        df.insert(0, 'category', i, allow_duplicates=False)
        df.insert(1, 'manufacturer', j.split('_')[1], allow_duplicates=False)
        df.insert(2, 'product', j.split('_')[2], allow_duplicates=False)
        df_list.append(df)

        preprocessing_df(df)

    df = pd.concat(df_list, ignore_index=True)
    df.to_csv('./csv_data/' + i + '.csv')
