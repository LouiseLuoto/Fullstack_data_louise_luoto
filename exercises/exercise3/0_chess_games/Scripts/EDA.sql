-- b) Find out the possible categories for winner column.
SELECT 
	winner
FROM
	chess
GROUP BY
	winner;
	

  -- c) Find out the possible categories for victory_status column.
SELECT 
    victory_status
FROM 
    chess
GROUP BY 
    victory_status;
    
   
  --d) Check total number of games represented in the dataset.
SELECT
    COUNT(*)
FROM
    chess;
    
   
 -- e) Get statistics on the number draws, the number of white wins and number of black wins.
SELECT
    winner,
    COUNT(*) AS "Number wins"
FROM
    chess
GROUP BY
    winner;
    
   
-- f) Check the top 10 most popular openings
SELECT
    opening_name,
    COUNT(*) AS "Number openings"
FROM
    chess
GROUP BY
    opening_name
ORDER BY
    "Number openings" DESC
LIMIT 10;


--g) Which player has the highest ranking?
SELECT player_id, MAX(rating) AS highest_rating
FROM (
    SELECT black_id AS player_id, black_rating AS rating FROM chess
    UNION
    SELECT white_id AS player_id, white_rating AS rating FROM chess
) AS combined_ratings
GROUP BY player_id
ORDER BY highest_rating DESC
LIMIT 1;

	