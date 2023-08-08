CREATE TABLE `States` (
  `StateID` int PRIMARY KEY,
  `StateName` varchar(255),
  `Abbreviation` varchar(255),
  `Population` int,
  `Capital` varchar(255),
  `Area` float
);

CREATE TABLE `Counties` (
  `CountyID` int PRIMARY KEY,
  `CountyName` varchar(255),
  `Population` int,
  `Area` float,
  `StateID` int
);

CREATE TABLE `Cities` (
  `CityID` int PRIMARY KEY,
  `CityName` varchar(255),
  `Population` int,
  `Area` int,
  `Latitude` float,
  `Longitude` float,
  `StateID` int,
  `CountyID` int
);

CREATE TABLE `CityCounties` (
  `CityCountyID` int PRIMARY KEY,
  `CityID` int,
  `CountyID` int
);

ALTER TABLE `Counties` ADD FOREIGN KEY (`StateID`) REFERENCES `States` (`StateID`);

ALTER TABLE `Cities` ADD FOREIGN KEY (`StateID`) REFERENCES `States` (`StateID`);

ALTER TABLE `Cities` ADD FOREIGN KEY (`CountyID`) REFERENCES `Counties` (`CountyID`);

ALTER TABLE `CityCounties` ADD FOREIGN KEY (`CityID`) REFERENCES `Cities` (`CityID`);

ALTER TABLE `CityCounties` ADD FOREIGN KEY (`CountyID`) REFERENCES `Counties` (`CountyID`);
