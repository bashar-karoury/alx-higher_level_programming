-- Lists all citys of California that can be found in database
-- from tables cities and states
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE state_id = (SELECT states.id FROM states WHERE states.name = 'California') ORDER BY cities.id ASC;
