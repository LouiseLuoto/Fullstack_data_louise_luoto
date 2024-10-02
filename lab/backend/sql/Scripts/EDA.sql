-- koden hämtar datum, antal visningar och visningstid från två tabeller och hoppar
-- över första raden. tabellerna kopplas sedan ihop och resultatet blir formaterade 
-- datum, visningar från båda tabellerna och visningstid i timmar från date_table.
WITH
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT
	STRFTIME('%Y-%m-%d', tot.datum),
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total AS tot
LEFT JOIN date_table AS tab
ON tot.datum = tab.datum;


-- antal visningar och antal rader per enhetstyp.
SELECT
	enhetstyp,
	COUNT(*) total_rows,
	SUM(Visningar) AS total_visningar
FROM
	enhetstyp.diagramdata
GROUP BY
	enhetstyp;


-- visar alla kolumner utom innehåll. sorterar resultatet efter fallande ordning på 
-- visningstid (timmar), hoppar över första raden och returnerar de följande 5.
SELECT
	* EXCLUDE (innehåll)
FROM
	innehall.tabelldata
ORDER BY
	"Visningstid (timmar)" DESC OFFSET 1
LIMIT 5;


-- visningstid (timmar) finns ej i innehall.diagramdata.
SELECT
	*
FROM
	innehall.diagramdata; -- ORDER BY "Visningstid (timmar)";


-- antalet visningar per dag.
SELECT
	STRFTIME('%Y-%m-%d',
	datum),
	Visningar
FROM
	innehall.totalt;


-- tabeller i innehall.
SELECT
	*
FROM
	innehall.tabelldata;


-- antal visningar per video.
SELECT
	Videotitel,
	Visningar
FROM
	innehall.tabelldata
ORDER BY
	Visningar DESC
OFFSET 1;


-- tittarnas kön och deras respektive andel av visningar i procent.
SELECT * FROM tittare.tabelldata_alder;

SELECT
	"Tittarnas kön",
	"Visningar (%)"
FROM
	tittare.tabelldata_alder;


-- tittarnas ålder och deras respektive andel av visningar i procent.
SELECT * FROM tittare.tabelldata_kon;

SELECT
	"Tittarnas ålder",
	"Visningar (%)"
FROM
	tittare.tabelldata_kon;


-- vilken typ av enhet tittaren använt.
SELECT * FROM enhetstyp.tabelldata;

SELECT
    Enhetstyp,
    Visningar
FROM
    enhetstyp.tabelldata;