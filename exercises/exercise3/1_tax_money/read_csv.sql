CREATE TABLE tax07 AS
SELECT *
FROM read_csv_auto('../../../data/leverantorsfaktura202407.csv', types={'Organisationsnummer': 'VARCHAR'})

CREATE TABLE tax08 AS
SELECT *
FROM read_csv_auto('../../../data/leverantorsfaktura202408.csv', types={'Organisationsnummer': 'VARCHAR'})