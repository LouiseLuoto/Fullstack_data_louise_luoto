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


--antal visningar och antal rader per enhetstyp
SELECT
	enhetstyp,
	COUNT(*) total_rows,
	SUM(Visningar) AS total_visningar
FROM
	enhetstyp.diagramdata
GROUP BY
	enhetstyp;


--visar alla kolumner utom innehåll. sorterar resultatet efter fallande ordning på 
--visningstid (timmar), hoppar över första raden och returnerar de följande 5
SELECT
	* EXCLUDE (innehåll)
FROM
	innehall.tabelldata
ORDER BY
	"Visningstid (timmar)" DESC OFFSET 1
LIMIT 5;

--Visningstid (timmar) finns ej i innehall.diagramdata
SELECT
	*
FROM
	innehall.diagramdata; -- ORDER BY "Visningstid (timmar)";


--antalet visningar per dag
SELECT
	STRFTIME('%Y-%m-%d',
	datum),
	Visningar
FROM
	innehall.totalt;


--vad innehåller innehall
SELECT
	*
FROM
	innehall.tabelldata;


--antal visningar per video
SELECT
	Videotitel,
	Visningar
FROM
	innehall.tabelldata
ORDER BY
	Visningar DESC
OFFSET 1;

--vad innehåller tittare.tabelldata_alder
SELECT
	*
FROM
	tittare.tabelldata_alder;


--procentuell visning av tittarnas kön
SELECT
	"Tittarnas kön",
	"Visningar (%)"
FROM
	tittare.tabelldata_alder;


--vad innehåller tittare.tabelldata_kon
SELECT
	*
FROM
	tittare.tabelldata_kon;


--procentuell visning av tittarnas ålder
SELECT
	"Tittarnas ålder",
	"Visningar (%)"
FROM
	tittare.tabelldata_kon;