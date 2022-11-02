-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- Lists all shows contained in the database hbtn_0d_tvshows
-- without a genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and
-- tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT s.title, g.genre_id
	FROM tv_shows AS s
		LEFT JOIN tv_show_genres AS g
		ON s.id = g.show_id
		WHERE g.genre_id IS NULL
	ORDER BY s.title, g.genre_id;
