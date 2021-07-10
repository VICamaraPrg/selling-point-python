CREATE DATABASE IF NOT EXISTS my_store
	CHARACTER SET utf8;

USE my_store;


CREATE TABLE IF NOT EXISTS product_category (
	id INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
    pc_name VARCHAR(30) DEFAULT NULL,
    
    CONSTRAINT product_category_id PRIMARY KEY(id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS product (
	ean13 CHAR(13) NOT NULL,
    short_ref VARCHAR(5) DEFAULT NULL UNIQUE,
    p_name VARCHAR(50) DEFAULT NULL,
    price DECIMAL(4,2) DEFAULT 0.0,
    stock INT(4) DEFAULT 100,
    category_id INT(3) UNSIGNED NOT NULL,
    
    CONSTRAINT product_ean13 PRIMARY KEY(ean13),
    CONSTRAINT product_category_id FOREIGN KEY (category_id)
		REFERENCES product_category(id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS worker (
	id CHAR(6) NOT NULL,
    w_name VARCHAR(30) DEFAULT NULL,
    surname VARCHAR(30) DEFAULT NULL,
    birth_date DATE DEFAULT NULL,
    password_hash CHAR(128) DEFAULT NULL,
    password_salt VARCHAR(60) DEFAULT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP DEFAULT NULL,
    
    CONSTRAINT worker_id PRIMARY KEY(id)
    
) ENGINE = InnoDB;
