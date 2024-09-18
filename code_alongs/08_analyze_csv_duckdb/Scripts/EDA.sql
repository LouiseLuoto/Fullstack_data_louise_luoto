SELECT * FROM youtube;

SELECT DISTINCT(category) FROM youtube;

SELECT COUNT(*)	FROM youtube;

-- how many in each category?
SELECT
	category, COUNT(*) AS number
FROM
	youtube
GROUP BY
	category
ORDER BY
	number DESC
LIMIT 10;