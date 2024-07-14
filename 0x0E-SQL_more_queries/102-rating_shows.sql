-- a script that uses the hbtn_0d_tvshows database to lists
-- Each record should display: tv_shows.title - rating sum

SELECT title, SUM(rate) AS rating FROM tv_shows, tv_show_ratings
WHERE tv_shows.id = tv_show_ratings.show_id GROUP BY title ORDER BY rating DESC;
