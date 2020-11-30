CREATE DATABASE yektanet;

CREATE TABLE Advertiser(
	ID		INT				NOT NULL UNIQUE,
	name	VARCHAR (100)	NOT NULL,
	clicks	INT				DEFAULT 0,
	views	INT				DEFAULT 0,
	PRIMARY KEY (ID)
);

CREATE TABLE Ad(
	ID				INT				NOT NULL UNIQUE,
	title			VARCHAR (500)	NOT NULL,
	imgUrl			VARCHAR (1000)	NOT NULL,
	link			VARCHAR (1000)	NOT NULL,
	clicks			INT				DEFAULT 0,
	views			INT				DEFAULT 0,
	advertiser_id	INT references Advertiser(ID),
	PRIMARY KEY (ID)
);