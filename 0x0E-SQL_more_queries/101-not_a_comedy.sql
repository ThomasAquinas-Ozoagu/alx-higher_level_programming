-- a script that uses the hbtn_0d_tvshows database to lists
-- tv_genres table contains only one record where name = Comedy
-- (but the id can be different)

SELECT title FROM tv_shows WHERE tv_shows.id NOT IN (
SELECT show_id FROM tv_show_genres JOIN tv_genres ON genre_id = tv_genres.id
WHERE name = 'COMEDY')
ORDER BY title;
