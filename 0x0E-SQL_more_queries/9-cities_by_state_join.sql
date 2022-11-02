-- Lists all cities contained in the database
-- Each record should display: cities.id -
-- cities.name - states.name
-- Results must sorted in ascending order cities.id
SELECT c.id, c.name, s.name
	FROM cities AS c
		INNER JOIN states AS s
		ON c.state_id = s.id
	ORDER BY c.id;
