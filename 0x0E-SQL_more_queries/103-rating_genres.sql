-- a script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating.
-- Each record should display: tv_genres.name - rating sum

SELECT name, SUM(rate) AS rating
FROM tv_genres, tv_show_ratings, tv_show_genres WHERE tv_genres.id = genre_id
AND tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name ORDER BY rating DESC;
