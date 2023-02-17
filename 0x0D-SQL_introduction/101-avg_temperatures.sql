-- display the average temperatures in descending order
SELECT DISTINCT city, AVG(value) AS avg_tmp 
FROM temperatures
GROUP BY city
ORDER BY avg_tmp DESC;
