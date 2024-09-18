-- Drop the database if it already exists
DROP DATABASE IF EXISTS Gans ;

-- Create the database
CREATE DATABASE Gans;

-- Use the database
USE Gans;

-- Create the 'City' table
CREATE TABLE city_info (
    city_id INT AUTO_INCREMENT, -- Automatically generated ID for each city
    city_name	 VARCHAR(255) NOT NULL, -- Name of the city
    Country  VARCHAR(255) NOT NULL, -- Name of the Country
    population INT, -- population of the city
    Longitude VARCHAR(15) NOT NULL, -- Longitude of the city   
    Latitude VARCHAR(15) NOT NULL, -- Latitude of the city 
    PRIMARY KEY (city_id) -- Primary key to uniquely identify each city
);

-- Create the 'weather' table
CREATE TABLE weather (
    weather_id INT AUTO_INCREMENT, -- Automatically generated ID for each record
    city_id INT,  -- Foreign key to the city_info table
    City VARCHAR(255) NOT NULL, -- Name of the city
    Forecast_item VARCHAR(255), -- Forecast information
    Temperature DECIMAL(5, 2), -- Temperature in degrees Celsius, with 2 decimal places
    Forecast VARCHAR(255), -- Description of the forecast 
    Rain_in_last_3h DECIMAL(5, 2), -- Amount of rain in the last 3 hours 
    Wind_speed DECIMAL(5, 2), -- Wind speed
    Data_retrieved_at DATETIME, -- Timestamp of when the data was retrieved
    PRIMARY KEY (weather_id), -- Primary key to uniquely identify each weather record
    FOREIGN KEY (city_id) REFERENCES city_info(city_id) -- Foreign key to the city_info table
);
-- Create the 'Airport' table
CREATE TABLE airport_info (
    airport_id INT AUTO_INCREMENT, -- Auto-incremented ID for each airport (primary key)
    city_id INT, -- Foreign key to link with the city_info table
    icao VARCHAR(10) NOT NULL, -- ICAO code of the airport
    iata VARCHAR(10), -- IATA code of the airport
    city_name VARCHAR(255) NOT NULL, -- Full name of the airport
    shortName VARCHAR(255), -- Short name of the airport
    municipalityName VARCHAR(255), -- Name of the municipality or city where the airport is located
    countrycode VARCHAR(5) NOT NULL, -- Country code of the airport
    timezone VARCHAR(50), -- Time zone of the airport
    location_lat DECIMAL(10, 6), -- Latitude of the airport's location
    location_lon DECIMAL(10, 6), -- Longitude of the airport's location
    localcode VARCHAR(10), -- Local code of the airport  
    PRIMARY KEY (airport_id), -- Primary key to uniquely identify each airport
    FOREIGN KEY (city_id) REFERENCES city_info(city_id) -- Foreign key to the city_info table
);
-- Create the 'flights' table
CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT, -- Auto-incremented ID for each flight (primary key)
    arrival_airport_icao VARCHAR(10) NOT NULL, -- ICAO code of the arrival airport
    departure_airport_icao VARCHAR(10) NOT NULL, -- ICAO code of the departure airport
    schedule_arrival_time DATETIME, -- Scheduled arrival time
    flight_number VARCHAR(20), -- Flight number
    airline VARCHAR(255), -- Airline name
    data_retrive_at DATETIME, -- Timestamp of when the data was retrieved
    city_id INT, -- Foreign key to reference the city
    PRIMARY KEY (flight_id), -- Primary key to uniquely identify each flight
    FOREIGN KEY (city_id) REFERENCES city_info(city_id) -- Foreign key to the city_info table
);

