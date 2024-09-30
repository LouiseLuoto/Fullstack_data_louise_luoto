### constants.py
Skapar sökväg till youtube_data.db och cleaned_data med hjälp av två variabler.


### change_name_data.py
Först kontrollerar vi om mappen cleaned_data finns. Gör den det raderas den. Sedan skapar vi en ny cleaned_data mapp. Kopierar alla mappar från raw_data och använder det första ordet i det ursprungliga namnet för varje fil.


### database.py
Database-klassen hanterar en anslutning till en DuckDB-databas. Den innehåller en metod för att köra SQL-frågor och context manager med hjälp av __enter__ och __exit__. Klassen DatabaseDataframe ärver från klassen Database och returnerar resultatet som en DataFrame iställer för en lista med resultat.


### ingest_data_to_database.py
Denna kod laddar in CSV-filer i databasen. Den första loopen går igenom alla kataloger i CLEANED_DATA_PATH. Varje katalognamn används som ett schema och varje CSV-fil skapar en motsvarande tabell i databasen. Det senare görs i andra loopen. Även å, ä och ö byts ut när schema- och tabellnamn skapas. 


### EDA SQL
--koden hämtar datum, antal visningar och visningstid från två tabeller och hoppar över första raden. --tabellerna kopplas sedan ihop och resultatet blir formaterade datum, visningar från båda tabellerna och --visningstid i timmar från date_table.
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


--visningstid (timmar) finns ej i innehall.diagramdata
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


--tabeller i innehall
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


--tabeller i tittare.tabelldata_alder
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


--tabeller i tittare.tabelldata_kon
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