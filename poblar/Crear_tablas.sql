CREATE TABLE Genero
(
	ClvGenero			NUMBER,
	Genero1			CHAR(64),
	Genero2			CHAR(64)		NOT NULL,
	Genero3			CHAR(64)		NOT NULL,
	PRIMARY KEY(ClvGenero));


CREATE TABLE MiembroCrew
(
	ClvMiembroCrew			NUMBER,
	EsGuionista			NUMBER(1),
	EsDirector			NUMBER(1),
	Nombre			CHAR(64),
	AnyoNacimiento			NUMBER		NOT NULL,
	AnyoFallecimiento			NUMBER		NOT NULL,
	PRIMARY KEY(ClvMiembroCrew));


CREATE TABLE MiembroCast
(
	ClvMiembroCast			NUMBER,
	NombrePersonaje			CHAR(80),
	Nombre			CHAR(64)		NOT NULL,
	AnyoNacimiento			NUMBER		NOT NULL,
	AnyoFallecimiento			NUMBER		NOT NULL,
	PRIMARY KEY(ClvMiembroCast));


CREATE TABLE Pelicula
(
	ClvPelicula			NUMBER,
	Titulo			CHAR(100)		NOT NULL,
	EsAdulta			NUMBER(1),
	Duracion			NUMBER,
	AnyoEstreno			NUMBER,
	PRIMARY KEY(ClvPelicula));


CREATE TABLE Fecha
(
	ClvFecha			NUMBER,
	Anyo			NUMBER,
	Mes			NUMBER,
	Dia			NUMBER,
	DiaMesAnyo			DATE,
	PRIMARY KEY(ClvFecha));


CREATE TABLE Crew
(
	ClvCrew			NUMBER,
	ClvMiembroCrew			NUMBER,
	PRIMARY KEY(ClvCrew,ClvMiembroCrew),
	FOREIGN KEY(ClvMiembroCrew) REFERENCES MiembroCrew (ClvMiembroCrew));

CREATE TABLE Cast
(
	ClvCast			NUMBER,
	ClvMiembroCast			NUMBER,
	PRIMARY KEY(ClvCast,ClvMiembroCast),
	FOREIGN KEY(ClvMiembroCast) REFERENCES MiembroCast (ClvMiembroCast));

CREATE TABLE Voto
(
	ClvVoto			NUMBER,
	ClvCrew			NUMBER		NOT NULL,
	ClvCast			NUMBER		NOT NULL,
	ClvPelicula			NUMBER		NOT NULL,
	ClvGenero			NUMBER		NOT NULL,
	ClvFecha			NUMBER		NOT NULL,
	UserName			NUMBER      NOT NULL,
	Puntuacion			FLOAT,
	PRIMARY KEY(ClvVoto),
	FOREIGN KEY(ClvPelicula) REFERENCES Pelicula (ClvPelicula),
	FOREIGN KEY(ClvGenero) REFERENCES Genero (ClvGenero),
	FOREIGN KEY(ClvFecha) REFERENCES Fecha (ClvFecha));

