-- a script that uses the hbtn_0d_tvshows database to lists
-- all genres of the show Dexter

SELECT name FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_shows.title = 'Dexter'
AND tv_genres.id = tv_show_genres.genre_id
AND show_id = tv_shows.id ORDER BY name;
