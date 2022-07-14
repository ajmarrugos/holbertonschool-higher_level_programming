-- Count the number of records with the same score in the table 'second_table' of the database.
SELECT score, count(score) as number FROM second_table GROUP BY score ORDER BY score DESC