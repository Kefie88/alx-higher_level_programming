-- Displays the maximum temperature of each state
-- ordered by state name
SELECT 'state', MAX('value') AS 'max_temp'
FROM 'temperaturres'
GROUP BY 'state'
ORDER BY 'state';
