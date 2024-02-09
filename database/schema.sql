DROP DATABASE IF EXISTS gotravel;
CREATE DATABASE gotravel;
DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
  country_id INT GENERATED ALWAYS AS IDENTITY,
  iso VARCHAR(2),
  country_name VARCHAR(50),
  continent VARCHAR(2),
  PRIMARY KEY (country_id)
);

CREATE TABLE cities (
  city_id INT,
  city_name VARCHAR(100),
  country_id INT,
  latitude DECIMAL(10, 6),
  longitude DECIMAL(10, 6),
  PRIMARY KEY (city_id),
  CONSTRAINT fk_country_id 
    FOREIGN KEY (country_id) 
    REFERENCES countries(country_id)
);

CREATE TABLE airports (
  airport_id INT GENERATED ALWAYS AS IDENTITY,
  iata VARCHAR(4) NOT NULL,
  airport_name VARCHAR(100),
  country_id INT,
  latitude DECIMAL(10, 6),
  longitude DECIMAL(10, 6),
  PRIMARY KEY (airport_id),
  CONSTRAINT fk_country_id 
    FOREIGN KEY (country_id) 
    REFERENCES countries(country_id)
);

