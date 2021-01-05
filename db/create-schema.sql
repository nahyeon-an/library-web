CREATE TABLE IF NOT EXISTS LIBRARY(
   libno            INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
   name             VARCHAR(50) NOT NULL,
   sido_nm          VARCHAR(10),
   gungu_nm         VARCHAR(10),
   close_day        VARCHAR(1000),
   every_open       VARCHAR(10),
   every_close      VARCHAR(10),
   sat_open         VARCHAR(10),
   sat_close        VARCHAR(10),
   holiday_open     VARCHAR(10),
   holiday_close    VARCHAR(10),
   seats            INTEGER,
   books            INTEGER,
   loanable_books   INTEGER,
   loanable_days    INTEGER,
   address          VARCHAR(100),
   phone_number     VARCHAR(20),
   site             VARCHAR(1000)
);

CREATE TABLE IF NOT EXISTS BLINDBOOK(
  bookno      INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
  author      VARCHAR(100) NOT NULL,
  title       VARCHAR(500) NOT NULL,
  publisher   VARCHAR(1000),
  isbn        VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS CITY(
  sido_nm          VARCHAR(10) NOT NULL,
  gungu_nm         VARCHAR(10) NOT NULL,
  libnumber        INTEGER,
  PRIMARY KEY (sido_nm, gungu_nm)
);

CREATE TABLE IF NOT EXISTS USER(
  id          VARCHAR(100) NOT NULL PRIMARY KEY,
  password    VARCHAR(100),
  name        VARCHAR(50),
  sido_nm     VARCHAR(10),
  gungu_nm    VARCHAR(10),
  address     VARCHAR(1000),
  email       VARCHAR(500)
);
