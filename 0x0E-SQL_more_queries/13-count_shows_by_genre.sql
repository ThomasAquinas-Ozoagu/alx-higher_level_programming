-- a script that lists all shows contained in hbtn_0d_tvshows
-- Each record should display: <TV Show genre> -
-- <Number of shows linked to this genre>

SELECT name AS genre, COUNT(show_id)
AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON id = genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
