-- LIST CITY BY AVG TEMP
-- LIST TEMP AVG in CITY
SELECT city, AVG(value) as average FROM temperatures GROUP BY (city) ORDER by average DESC;
