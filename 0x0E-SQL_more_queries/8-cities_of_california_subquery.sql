-- Lists all citys of California that can be found in database
-- from tables cities and states
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
