CREATE TABLE `product_category` (
	`category_index` int NOT NULL,
	`category_name`	varchar(100) NULL UNIQUE
);

CREATE TABLE `product` (
	`product_index`	int NOT NULL,
	`category_index` int	NOT NULL,
	`product_name`	varchar(100)	NULL UNIQUE,
	`product_manufacturer`	varchar(100)	NULL
);

CREATE TABLE `product_review` (
	`product_review_index`	int	NOT NULL,
	`product_index`	int	NOT NULL,
	`category_index`	int	NOT NULL,
	`review_writer_name`	varchar(100)	NULL
);

CREATE TABLE `review_analyzing_data` (
	`product_review_index`	int	NOT NULL,
	`product_index`	int	NOT NULL,
	`category_index`	int	NOT NULL,
	`review_date`	date	NOT NULL,
	`review_rating`	int	NOT NULL,
	`newline_count`	int	NULL,
	`review_len`	int	NULL,
	`special_char_count`	int	NULL,
	`manufacturer_count`	int	NULL,
	`product_count`	int	NULL
);

CREATE TABLE `review_content` (
	`product_review_index`	int	NOT NULL,
	`product_index`	int	NOT NULL,
	`category_index`	int	NOT NULL,
	`review_content`	text	NULL
);

CREATE TABLE `csv_save` (
	`review_index`	int	NULL,
	`category`	varchar(100)	NULL,
	`manufacturer`	varchar(100)	NULL,
	`product`	varchar(100)	NULL,
	`writer_name`	varchar(100)	NULL,
	`review_date`	date	NOT NULL,
	`rating`	int	NOT NULL,
	`review_content`	text	NULL,
	`newline_count`	int	NULL,
	`review_len`	int	NULL,
	`special_char_count`	int	NULL,
	`manufacturer_count`	int	NULL,
	`product_count`	int	NULL
);

ALTER TABLE `product_category` ADD CONSTRAINT `PK_PRODUCT_CATEGORY` PRIMARY KEY (
	`category_index`
);

ALTER TABLE `product` ADD CONSTRAINT `PK_PRODUCT` PRIMARY KEY (
	`product_index`,
	`category_index`
);

ALTER TABLE `product_review` ADD CONSTRAINT `PK_PRODUCT_REVIEW` PRIMARY KEY (
	`product_review_index`,
	`product_index`,
	`category_index`
);

ALTER TABLE `review_analyzing_data` ADD CONSTRAINT `PK_REVIEW_ANALYZING_DATA` PRIMARY KEY (
	`product_review_index`,
	`product_index`,
	`category_index`
);

ALTER TABLE `review_content` ADD CONSTRAINT `PK_REVIEW_CONTENT` PRIMARY KEY (
	`product_review_index`,
	`product_index`,
	`category_index`
);

ALTER TABLE `product_category` MODIFY `category_index` INT NOT NULL AUTO_INCREMENT;

ALTER TABLE `product` MODIFY `product_index` INT NOT NULL AUTO_INCREMENT;

ALTER TABLE `product` ADD CONSTRAINT `FK_product_category_TO_product_1` FOREIGN KEY (
	`category_index`
)
REFERENCES `product_category` (
	`category_index`
);

ALTER TABLE `product_review` ADD CONSTRAINT `FK_product_TO_product_review_1` FOREIGN KEY (
	`product_index`
)
REFERENCES `product` (
	`product_index`
);

ALTER TABLE `product_review` ADD CONSTRAINT `FK_product_TO_product_review_2` FOREIGN KEY (
	`category_index`
)
REFERENCES `product` (
	`category_index`
);

ALTER TABLE `review_analyzing_data` ADD CONSTRAINT `FK_product_review_TO_review_analyzing_data_1` FOREIGN KEY (
	`product_review_index`
)
REFERENCES `product_review` (
	`product_review_index`
);

ALTER TABLE `review_analyzing_data` ADD CONSTRAINT `FK_product_review_TO_review_analyzing_data_2` FOREIGN KEY (
	`product_index`
)
REFERENCES `product_review` (
	`product_index`
);

ALTER TABLE `review_analyzing_data` ADD CONSTRAINT `FK_product_review_TO_review_analyzing_data_3` FOREIGN KEY (
	`category_index`
)
REFERENCES `product_review` (
	`category_index`
);

ALTER TABLE `review_content` ADD CONSTRAINT `FK_product_review_TO_review_content_1` FOREIGN KEY (
	`product_review_index`
)
REFERENCES `product_review` (
	`product_review_index`
);

ALTER TABLE `review_content` ADD CONSTRAINT `FK_product_review_TO_review_content_2` FOREIGN KEY (
	`product_index`
)
REFERENCES `product_review` (
	`product_index`
);

ALTER TABLE `review_content` ADD CONSTRAINT `FK_product_review_TO_review_content_3` FOREIGN KEY (
	`category_index`
)
REFERENCES `product_review` (
	`category_index`
);

