### constants.py
Skapar sökväg till youtube_data.db och cleaned_data med hjälp av två variabler.


### change_name_data.py
Först kontrollerar vi om mappen cleaned_data finns. Gör den det raderas den. Sedan skapar vi en ny cleaned_data mapp. Kopierar alla mappar från raw_data och använder det första ordet i det ursprungliga namnet för varje fil.


### database.py
Database-klassen hanterar en anslutning till en DuckDB-databas. Den innehåller en metod för att köra SQL-frågor och context manager med hjälp av __enter__ och __exit__. Klassen DatabaseDataframe ärver från klassen Database och returnerar resultatet som en DataFrame iställer för en lista med resultat.


### ingest_data_to_database.py
Denna kod laddar in CSV-filer i databasen. Den första loopen går igenom alla kataloger i CLEANED_DATA_PATH. Varje katalognamn används som ett schema och varje CSV-fil skapar en motsvarande tabell i databasen. Det senare görs i andra loopen. Även å, ä och ö byts ut när schema- och tabellnamn skapas. 


### EDA SQL
Koden hämtar datum, antal visningar och visningstid från två tabeller och hoppar över första raden. Tabellerna kopplas sedan ihop och resultatet blir formaterade datum, visningar från båda tabellerna och visningstid i timmar från date_table.


Antal visningar och antal rader per enhetstyp.


Visar alla kolumner utom innehåll. Sorterar resultatet efter fallande ordning på visningstid (timmar), hoppar över första raden och returnerar de följande 5.


Visningstid (timmar) finns ej i innehall.diagramdata.


Antal visningar per dag.


Alla tabeller i innehall.


Antal visningar per video. 


Tittarnas kön och deras respektive andel av visningar i procent.


Tittarnas ålder och deras respektive andel av visningar i procent.


Vilken typ av enhet tittaren använt.