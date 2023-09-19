-- Creates a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant priviledges on database to user
GRANT ALL PRIVILEGES
ON hbnb_test_db .*
TO 'hbnb_test'@'localhost';

-- Grant select privileges on database performance schema to user
GRANT SELECT
ON performance_schema .*
TO 'hbnb_test'@'localhost';
