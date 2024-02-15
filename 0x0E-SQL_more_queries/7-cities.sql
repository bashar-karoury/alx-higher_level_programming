-- Creates database and  user in data base with all privileges
-- create user with its privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(state_id)
);
