-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy
-- (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT DISTINCT title
	FROM tv_shows AS t
		LEFT JOIN tv_show_genres AS s
		ON s.show_id = t.id

		LEFT JOIN tv_genres AS g
		ON g.id = s.genre_id
		WHERE t.title NOT IN
			(SELECT title
				FROM tv_shows AS t
				INNER JOIN tv_show_genres AS s
				ON s.show_id = t.id

				INNER JOIN tv_genres AS g
				ON g.id = s.genre_id
				WHERE g.name = "Comedy")
	ORDER BY title;