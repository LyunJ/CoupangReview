select review_rating, avg((if(special_char_count = 0,1,special_char_count) * if(manufacturer_count = 0,1,manufacturer_count) * if(product_count = 0,1,product_count)) / if(review_len = 0, 1, review_len)) as c1
from review_analyzing_data 
where product_count >= 1 and review_len <> 0
group by review_rating
order by review_rating desc;

select a.*, max(a.review_date), min(a.review_date), (max(a.review_date) - min(a.review_date)) / (review_count_in_same_review * 100) as result
from (select a.category_index,a.product_index,a.review_writer_name,b.review_date,count(*) over (partition by a.review_writer_name,a.product_index) as review_count_in_same_review
 from product_review a left outer join review_analyzing_data b 
 on a.product_review_index = b.product_review_index
 and a.product_index = b.product_index
 and a.category_index = b.category_index) a
 where review_count_in_same_review >= 2 and a.review_writer_name not like '%*%' and a.review_writer_name not like '쿠팡실구매자'
 group by product_index,review_writer_name
 having result <> 0;

select a.*, max(a.review_date), min(a.review_date), (max(a.review_date) - min(a.review_date)) / (review_count_in_same_review * 100) as result
from (select a.category_index,a.product_index,a.review_writer_name,b.review_date,count(*) over (partition by a.review_writer_name,a.product_index) as review_count_in_same_review
 from product_review a left outer join review_analyzing_data b 
 on a.product_review_index = b.product_review_index
 and a.product_index = b.product_index
 and a.category_index = b.category_index) a
 where review_count_in_same_review >= 2
 group by product_index,review_writer_name
 having result <> 0;
 
 select review_date,count(*),dayofweek(review_date), avg(review_rating) as av
 from review_analyzing_data 
 group by review_date 
 having av >= 4
 order by 2 desc;

select count(distinct review_writer_name) from product_review
where review_writer_name not like '%*%' and review_writer_name not like '쿠팡실구매자';

select category,count(*)
from (select category, count(*) as c1 
from csv_save 
where review_len <> 0 and writer_name not like '%*%' and writer_name not like '쿠팡실구매자' 
group by writer_name, product, review_date 
having c1 >= 2) a
group by category;

select a.*
from (select *, count(*) over(partition by writer_name, product, review_date) as c1 
from csv_save 
where review_len <> 0 and writer_name not like '%*%' and writer_name not like '쿠팡실구매자') a
where c1 >=2
order by writer_name, product, review_date;

select review_rating, count(*) from review_analyzing_data where review_len <> 0 group by review_rating;

select dayofweek(review_date) as day, count(*) from review_analyzing_data where review_len <> 0 group by day;

select * from review_analyzing_data where review_len <> 0;

SELECT group_concat(`COLUMN_NAME`)
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='coupang_review' 
    AND `TABLE_NAME`='review_analyzing_data';
    
select rating,review_content from csv_save where rating =1 or rating=5;

use coupang_review;
select user, host from user;

create user 'doge1'@'183.97.18.77' identified by '12345';
grant select on coupang_review.* to 'doge1' @'183.97.18.77';
show grants for 'doge1'@'183.97.18.77';

create user 'doge2'@'125.142.65.128' identified by '12345';
grant select on coupang_review.* to 'doge2' @'125.142.65.128';
show grants for 'doge2'@'125.142.65.128';

create user 'doge3'@'121.133.115.52' identified by '12345';
grant select on coupang_review.* to 'doge3' @'121.133.115.52';
show grants for 'doge3'@'121.133.115.52';
flush privileges;

show variables like 'port';

select rating,review_content from csv_save where (rating =1 or rating=5) and review_len <> 0