-- Lists all cities of California
-- The states table contains only one record where name = California
-- Result must be sorted in ascending order by cities.id
SELECT id, name FROM cities
	WHERE state_id IN
		(SELECT id
			FROM states
			WHERE name = "California")
	ORDER BU id;
