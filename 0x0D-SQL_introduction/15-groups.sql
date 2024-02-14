-- Group by score
-- Group records with same score in second_table
SELECT score, COUNT(*) As number FROM second_table GROUP BY score;
