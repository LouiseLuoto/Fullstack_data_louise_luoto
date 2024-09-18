-- b) Find out the possible categories for winner column.
SELECT 
	winner, COUNT(*)
FROM
	chess
GROUP BY
	winner;