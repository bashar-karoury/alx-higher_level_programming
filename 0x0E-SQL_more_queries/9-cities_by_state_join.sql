-- Lists all citys of California that can be found in database
-- from tables cities and states
SELECT cities.id, cities.name, states.name FROM cities JOIN states WHERE cities.state_id = states.id ORDER BY cities.id ASC;
