-- Script that creates a table second_table with description:
-- id INT, name VARCHAR(256) and score INT
-- If table exists, shoul not fail
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table VALUES(1, 'John', 10);
INSERT INTO second_table VALUES(2, 'Alex', 3);
INSERT INTO second_table VALUES(3, 'Bob', 14);
INSERT INTO second_table VALUES(4, 'George', 8);
