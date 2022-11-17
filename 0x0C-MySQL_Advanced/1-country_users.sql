-- creates a table users
-- id(int PK), email(str), name(str), country
CREATE TABLE IF NOT EXISTS users (
       id int NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
       email varchar(255) NOT NULL UNIQUE,
       name varchar(255),
       country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL);