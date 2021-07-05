
import pymysql.cursors
import pandas as pd
import os
import re

csv_list_tmp = os.listdir('./csv_data/')
csv_list = [csv_file for csv_file in csv_list_tmp if re.search(
    '\.csv$', csv_file) != None]


for csv_filename in csv_list:
    csv_data = pd.read_csv(f'./csv_data/{csv_filename}')
    csv_data.rename(columns={'Unnamed: 0': 'review_index'}, inplace=True)

    conn = pymysql.connect(host='localhost',
                           user='유저이름',
                           password='비밀번호',
                           db='coupang_review',  # coupang_review 스키마 생성 필요
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

    try:
        with conn.cursor() as curs:
            # 빈 리스트 생성
            sql_rows = []
            row_length = len(csv_data)
            print(row_length)
            for row in range(row_length):
                # 리스트에 한줄씩 추가
                review_content = str(csv_data['text'][row]).replace('\"', '')
                sql_row = f"({csv_data['review_index'][row]},'{csv_data['category'][row]}','{csv_data['manufacturer'][row]}','{csv_data['product'][row]}','{csv_data['name'][row]}','{csv_data['date'][row]}',{csv_data['rating'][row]:d},\"{review_content}\",{csv_data['newline_count'][row]:d},{csv_data['review_len'][row]:d},{csv_data['special_char_count'][row]:d},{csv_data['manufacturer_count'][row]:d},{csv_data['product_count'][row]: d})"
                sql_rows.append(sql_row)

                # 10000개가 채워졌을 경우 db에 한번에 업로드
                if len(sql_rows) >= 10000:
                    sql = "INSERT INTO csv_save(review_index, category, manufacturer, product, writer_name, review_date, rating, review_content, newline_count, review_len, special_char_count, manufacturer_count, product_count) VALUES " + \
                        ",".join(sql_rows)
                    curs.execute(sql)
                    conn.commit()
                    sql_rows = []
            # 나머지행 db에 업로드
            if sql_rows:
                sql = "INSERT INTO csv_save(review_index, category, manufacturer, product, writer_name, review_date, rating, review_content, newline_count, review_len, special_char_count, manufacturer_count, product_count) VALUES " + \
                    ",".join(sql_rows)
                curs.execute(sql)
                conn.commit()
    except:
        continue
    finally:
        conn.close()
