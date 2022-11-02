-- Creates the MySQL server user user_0d_1
-- user_0d_1 should have privileges on your MySQL server
-- user_0d_1 password should be set to user_0d_1_pwd
-- If user exists, your script should not fail
CREATE USER IF NOT EXITS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhost';
