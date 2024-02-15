-- Creates database and  user in data base with all privileges
-- create user with its privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT PRIVILEGES ON *.* TO user_0d_2@localhost

