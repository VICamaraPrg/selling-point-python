USE mysql;

CREATE USER 'storemanager'@'localhost' IDENTIFIED BY 'managerpassword';
GRANT ALL PRIVILEGES ON my_store.* TO 'storemanager'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;