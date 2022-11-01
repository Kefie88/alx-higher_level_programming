--Displays average temperature
--By city order by descending temperature
SELECT 'city', AVG('value') AS 'avg_temp'
FROM 'temperatures'
GROUP BY 'city'
ORDER BY 'avg_temp' DESC;
