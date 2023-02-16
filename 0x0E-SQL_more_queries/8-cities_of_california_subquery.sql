-- lists all cities of california that can be found in tdatabase hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
);
