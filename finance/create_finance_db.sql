CREATE DATABASE IF NOT EXISTS financial_db;
USE financial_db;

CREATE TABLE historical (
    date DATETIME,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume FLOAT,
    dividends FLOAT,
    `stock splits` FLOAT,
    ticker VARCHAR(10),
    cpi FLOAT,
    unrate FLOAT,
    csi FLOAT
);

SELECT * FROM historical as h;

ALTER TABLE historical CHANGE stock_splits `stock splits` FLOAT;