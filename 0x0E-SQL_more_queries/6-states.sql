-- a script that creates the table id_not_null on your MySQL server.
-- The database name will be passed as an argument

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name VARCHAR(256) NOT NULL);
