-- LIST CITY BY AVG TEMP
-- LIST TEMP AVG in CITY
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER by state;
