CREATE DATABASE loginserver;

CREATE TABLE `loginserver`.`apps` (
	id 		int PRIMARY KEY AUTO_INCREMENT,
	nombre	varchar(200) NOT NULL,
	host	varchar(200) NOT NULL
) ENGINE=MyISAM;

CREATE TABLE `loginserver`.`users` (
	id		varchar(100) PRIMARY KEY,
	passwd	char(128) NOT NULL,
	activo	boolean DEFAULT TRUE
) ENGINE=MyISAM;

CREATE TABLE `loginserver`.`userapps` (
	user_id	varchar(100) NOT NULL,
	app_id	int NOT NULL
) ENGINE=MyISAM;