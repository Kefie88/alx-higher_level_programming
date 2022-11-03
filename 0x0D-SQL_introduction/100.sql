-- Convert the entire database hbtn_0c_0 to UTF8
ALTER DATABASE
	hbtn_0c_0
	CHARACTER SET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

-- convert table "first_table' to UTF8
ALTER TABLE
	hbtn_0c_0.first_table
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

-- convert column 'name' to UTF8
ALTER TABLE
	hbtn_0c_0.first_table
	MODIFY name
	VARCHAR(256)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
