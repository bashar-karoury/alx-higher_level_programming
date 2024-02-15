-- Lists all citys of California that can be found in database
-- from tables cities and states
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') SORTED BY cities.id ASC;
