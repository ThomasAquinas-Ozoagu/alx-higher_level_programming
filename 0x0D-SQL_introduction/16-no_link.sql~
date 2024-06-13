-- a script that lists the number of records with the same score in the table
-- The database name will be passed as argument of mysql command
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score HAVING number > 0  ORDER BY number DESC;
