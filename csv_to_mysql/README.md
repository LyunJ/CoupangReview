# mysql에 csv 데이터 등록하기

1. mysql에 coupang_review 스키마 생성
2. create_table.sql 쿼리 전체 실행
3. save_csv_to_other_tables_trigger.sql 파일의 트리거 생성 쿼리 실행
4. csv_to_mysql.py의 유저이름과 패스워드 기입
5. python csv_to_mysql.py

## 주의할 점

csv 파일의 인덱스 컬럼의 이름이 'Unknown: 0' 이 아닌 경우 무시하도록 하였음
현재 도서음반DVD.csv는 해당 이유로 무시됨
