-- displays max temperature of each state (ordered by states)
SELECT DISTINCT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
