-- list all number of records with thesame score in second_table
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
