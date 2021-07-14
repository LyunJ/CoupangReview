# 테이블 전체 데이터 삭제
delete from review_content;
delete from review_analyzing_data;
delete from product_review;
delete from product;
delete from product_category;
delete from csv_save;
alter table product_category auto_increment = 0;
alter table product auto_increment = 0;

# 트리거 삭제
drop trigger if exists insertTrigger;

# 트리거 등록
DELIMITER $$
CREATE TRIGGER insertTrigger
AFTER INSERT ON csv_save
FOR EACH ROW
BEGIN
declare new_category_id, new_product_id int default 0;

insert into product_category (category_name) values (NEW.category) on duplicate key update category_name = NEW.category;

set new_category_id := (select last_insert_id());

if (new_category_id = 0) then
begin
set new_category_id := (select category_index from product_category where category_name = NEW.category);
end;
end if;

insert into product (category_index,product_name,product_manufacturer) values(new_category_id,NEW.product,NEW.manufacturer) on duplicate key update product_name = NEW.product;

set new_product_id := (select last_insert_id());
if (new_product_id = 0) then
begin
set new_product_id := (select product_index from product where product_name = NEW.product);
end;
end if;

insert into product_review (product_review_index,product_index,category_index,review_writer_name) values(NEW.review_index,new_product_id,new_category_id,NEW.writer_name);
insert into review_analyzing_data (product_review_index, product_index, category_index, review_date, review_rating, newline_count, review_len, special_char_count, manufacturer_count, product_count)
values (NEW.review_index,new_product_id,new_category_id,NEW.review_date,NEW.rating,NEW.newline_count,NEW.review_len,NEW.special_char_count,NEW.manufacturer_count,NEW.product_count);
insert into review_content (product_review_index,product_index,category_index,review_content)
values (NEW.review_index,new_product_id,new_category_id,NEW.review_content);
END $$
DELIMITER ;



DELIMITER $$
CREATE TRIGGER insertTrigger
AFTER INSERT ON csv_save
FOR EACH ROW
BEGIN
declare new_category_id, new_product_id int default 0;

insert into product_category (category_name) values (NEW.category) on duplicate key update category_name = NEW.category;

set new_category_id := (select last_insert_id());

if (new_category_id = 0) then
begin
set new_category_id := (select category_index from product_category where category_name = NEW.category);
end;
end if;

insert into product (category_index,product_name,product_manufacturer) values(new_category_id,NEW.product,NEW.manufacturer) on duplicate key update product_name = NEW.product;

set new_product_id := (select last_insert_id());
if (new_product_id = 0) then
begin
set new_product_id := (select product_index from product where product_name = NEW.product);
end;
end if;

insert into product_review (product_review_index,product_index,category_index,review_writer_name) values(NEW.review_index,new_product_id,new_category_id,NEW.writer_name);
insert into review_analyzing_data (SELECT group_concat(`COLUMN_NAME`)
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='coupang_review' 
    AND `TABLE_NAME`='review_analyzing_data')
values (NEW.review_index,new_product_id,new_category_id,NEW.review_date,NEW.rating,NEW.newline_count,NEW.review_len,NEW.special_char_count,NEW.manufacturer_count,NEW.product_count);
insert into review_content (product_review_index,product_index,category_index,review_content)
values (NEW.review_index,new_product_id,new_category_id,NEW.review_content);
END $$
DELIMITER ;
