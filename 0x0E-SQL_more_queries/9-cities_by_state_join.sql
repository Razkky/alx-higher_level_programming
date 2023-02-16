-- list all cities contained in the database
-- reocrd should display cities.id, cities.name, states.name
-- sorted  by cities.id
SELECT c.id, c.name, s.name
FROM states AS s
JOIN cities AS c
ON c.state_id = s.id
ORDER BY c.id ASC;
