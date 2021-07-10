USE my_store;

INSERT INTO worker (id, w_name, surname, birth_date, password_hash, password_salt, created) VALUES
(123456, 'Ashley', 'MacArthur', '1989-10-09', 'reset_password', CONCAT(surname, SUBSTR(w_name,1,3)), CURDATE()),
(124578, 'Michael', 'Mayers', '1991-02-04', 'reset_password', CONCAT(surname, SUBSTR(w_name,1,3)), CURDATE());

INSERT INTO product_category(id, pc_name) VALUES
(1, 'Bread'),
(2, 'Cereal'),
(3, 'Juice'),
(4, 'Cosmetic'),
(5, 'Hygiene'),
(6, 'Baby'),
(7, 'Soda'),
(8, 'Water'),
(9, 'Beer'),
(10, 'Chips'),
(11, 'Ice Cream'),
(12, 'Meat'),
(13, 'Fish'),
(14, 'Cheese'),
(15, 'Iogurt'),
(16, 'Pet Food');

INSERT INTO product VALUES
(8178360705320,250,'Baguette 250gr',0.40,100,1),
(9698408698037,350,'Baguette 350gr',0.75,100,1),
(5576149204786,2300,'Baguette Pack-2 300gr',1.00,100,1),
(7126840105078,125,'Mini Baguette 125gr',0.15,100,1),
(3865889288670,500,'Big Baguette 500gr',0.80,100,1),
(6346752262686,76566,'Pita Pack-3',1.79,100,1),
(4541511421783,18601,'Bread Roll',0.25,100,1),
(2591923743228,880,'Russian Blini Pack-6',1.20,100,1),
(2540249007408,89849,'Burguer Bread Pack-4',1.25,100,1),
(3846364693270,6863,'Hot Dog Bread Pack-6',1.50,100,1),
(7864100598258,9398,'Mold Bread 12 Slices',1.00,100,1),
(6400466855773,21276,'Mold Bread 18 Slices',1.30,100,1),
(9816644468413,49675,'Mold Bread 24 Slices',1.80,100,1),
(6964279724922,58600,'Toast Ready Bread 24un',2.50,100,1);