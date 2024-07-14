-- a script that uses the hbtn_0d_tvshows database to lists
-- all genres of the show Dexter

SELECT title FROM tv_shows, tv_show_genres, tv_genres
WHERE name = 'Comedy'
AND tv_genres.id = tv_show_genres.genre_id
AND show_id = tv_shows.id ORDER BY title;
