-- a script that uses the hbtn_0d_tvshows database to lists
-- all genres of the show Dexter

 SELECT DISTINCT title,
 CASE WHEN genre_id IS NULL THEN NULL ELSE name END AS name
 FROM tv_genres, tv_shows LEFT JOIN tv_show_genres ON id = show_id
 WHERE tv_genres.id = genre_id OR genre_id IS NULL ORDER BY title, name;
