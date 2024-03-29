-- lists all shows contained in hbtn_0d_tvshows that have no genre
-- linkded sorted by show title and genre id
 SELECT tv_genres.name, COUNT(tv_genres.id) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.id, tv_genres.name ORDER BY number_of_shows DESC;
