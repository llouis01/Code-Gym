CREATE DATABASE stocks-data;
USE stocks-data;

CREATE TABLE stock-prices(
    id INT AUTO_INCREMENTAL PRIMARY KEY,
    symbol VARCHAR(10),
    timestamp DATETIME,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume FLOAT,
);