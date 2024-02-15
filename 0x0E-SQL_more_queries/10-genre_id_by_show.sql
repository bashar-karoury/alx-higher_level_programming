-- lists all shows contained in hbtn_0d_tvshows that have at least one genre
-- linkded sorted by show title and genre id
USE hbtn_0d_tvshows;
SELECT title, tv_genres.id AS genre_id FROM tv_shows JOIN tv_show_genres JOIN tv_genres ON tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
