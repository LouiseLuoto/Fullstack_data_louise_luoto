SELECT
	*
FROM
	information_schema.schemata
WHERE
	catalog_name = 'youtube_data';
	

CREATE SCHEMA IF NOT EXISTS marts;


CREATE TABLE IF NOT EXISTS marts.content_view_time AS
(
SELECT
	Videotitel,
	"Publiceringstid för video" AS Publiceringstid,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	Exponeringar,
	Prenumeranter,
	"Klickfrekvens för exponeringar (%)" AS "Klickfrekvens_exponering_%"
FROM
	 innehall.tabelldata
ORDER BY
	"Visningstid (timmar)" DESC OFFSET 1
);


SELECT * FROM marts.content_view_time;


CREATE TABLE IF NOT EXISTS marts.views_per_date AS (
SELECT
	STRFTIME('%Y-%m-%d', 
	Datum) AS Datum,
	Visningar
FROM
	innehall.totalt
);


SELECT * FROM information_schema.tables WHERE table_schema = 'marts';


SELECT * FROM marts.views_per_date;


CREATE TABLE IF NOT EXISTS marts.viewers_gender AS
(
SELECT
	"Tittarnas kön",
	"Visningar (%)"
FROM
	tittare.tabelldata_alder
);


CREATE TABLE IF NOT EXISTS marts.viewers_age AS
(
SELECT
	"Tittarnas ålder",
	"Visningar (%)"
FROM
	tittare.tabelldata_kon
);


SELECT * FROM trafikkalla.tabelldata;

CREATE TABLE IF NOT EXISTS marts.traffic_source AS
(
SELECT 
	Trafikkälla,
	Visningar,
	"Visningstid (timmar)",
	"Genomsnittlig visningslängd"
FROM
	trafikkalla.tabelldata
);


SELECT * FROM marts.traffic_source;


--avrunda timmar i visningstid (timmar)
SELECT * FROM marts.traffic_source

UPDATE marts.traffic_source 
SET "Visningstid (timmar)" = ROUND("Visningstid (timmar)");

--ta bort kolumn genomsnittlig visningslängd
ALTER TABLE marts.traffic_source 
DROP COLUMN "Genomsnittlig visningslängd";


--skapa tabell visningar per video
SELECT * FROM innehall.tabelldata;   

CREATE TABLE IF NOT EXISTS marts.views_per_video AS
(
SELECT
    Videotitel, 
    Visningar
FROM
    innehall.tabelldata OFFSET 1
LIMIT (SELECT COUNT(*) FROM innehall.tabelldata) - 7);


SELECT * FROM marts.views_per_video;


SELECT * FROM enhetstyp.tabelldata;

CREATE TABLE IF NOT EXISTS marts.views_by_device AS
(
SELECT
	Enhetstyp,
	Visningar,
	ROUND("Visningstid (timmar)") AS "Visningstid (timmar)"
FROM
	enhetstyp.tabelldata OFFSET 1);

SELECT * FROM marts.views_by_device;