SELECT airport_name, countries.country_name FROM airports
JOIN countries ON airports.country_id = countries.country_id
WHERE iata LIKE 'EAB';