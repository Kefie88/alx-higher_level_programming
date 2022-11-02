-- Creates table id_not_null on your MySQL server
-- id INT with default value 1 and name VARCHAR(256)
CREATE TABLE IF NOT EXIST 'id_not_null' (
	'id' INT DEFAULT 1, 'name' VARCHAR(256)
);
