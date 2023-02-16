-- Creat a database called hbtn_0d_2 and user_0d_2 with select privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
