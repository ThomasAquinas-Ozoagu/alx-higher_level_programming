-- a script that uses the hbtn_0d_tvshows database to lists
-- all genres of the show Dexter

SELECT name FROM tv_genres WHERE tv_genres.id NOT IN (
SELECT genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = show_id
WHERE tv_shows.title = 'DEXTER') ORDER BY name;
