-- lists all shows from database by their rating
SELECT title, SUM(rate) as rating
FROM tv_shows as ts
JOIN tv_show_ratings as tsr
ON ts.id = tsr.show_id
GROUP BY title
ORDER BY rating DESC;
