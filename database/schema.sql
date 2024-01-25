DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS countries;


CREATE TABLE airports (
  airport_id INT GENERATED ALWAYS AS IDENTITY,
  iata VARCHAR(4) NOT NULL,
  airport_name VARCHAR(100),
  iso VARCHAR(3),
  latitude DECIMAL(10, 6),
  longitude DECIMAL(10, 6),
  PRIMARY KEY (airport_id)
);


CREATE TABLE countries (
  country_id INT GENERATED ALWAYS AS IDENTITY,
  iso VARCHAR(3),
  country_name VARCHAR(100),
  continent VARCHAR(20),
  PRIMARY KEY (country_id)
);