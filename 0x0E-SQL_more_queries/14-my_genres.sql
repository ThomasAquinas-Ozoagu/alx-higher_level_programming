-- The tv_shows table contains only one record where title = Dexter
-- (but the id can be different)

SELECT name FROM tv_genres
WHERE id IN (SELECT genre_id FROM tv_show_genres
WHERE show_id = (SELECT id FROM tv_shows
WHERE title = 'Dexter'))
ORDER BY name;
