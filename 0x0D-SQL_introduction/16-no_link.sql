--  Lists all records of the table 'second_table' of the database.
select score, name FROM second_table WHERE name IS NOT NULL order by score DESC;