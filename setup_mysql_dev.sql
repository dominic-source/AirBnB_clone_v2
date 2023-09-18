-- This script prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- -- creating new user named : hbnb_dev with the password : hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
-- granting the SELECT privilege in the db performance_schema
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
