CREATE TABLE `States` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `abbreviation` varchar(255),
  `population` int,
  `capital` varchar(255),
  `area` float
);

CREATE TABLE `Counties` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `population` int,
  `area` float,
  );

CREATE TABLE `Cities` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `population` int,
  `area` int,
  `latitude` float,
  `longitude` float
)



ALTER TABLE `Counties` ADD FOREIGN KEY (`StateID`) REFERENCES `States` (`StateID`);

ALTER TABLE `Cities` ADD FOREIGN KEY (`StateID`) REFERENCES `States` (`StateID`);

ALTER TABLE `Cities` ADD FOREIGN KEY (`CountyID`) REFERENCES `Counties` (`CountyID`);

