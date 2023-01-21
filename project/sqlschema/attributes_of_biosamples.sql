

CREATE TABLE "Biosample" (
	id TEXT NOT NULL, 
	depth TEXT, 
	intval INTEGER NOT NULL, 
	sometimes_absent TEXT NOT NULL, 
	lat FLOAT, 
	PRIMARY KEY (id)
);

CREATE TABLE "BiosampleCollection" (
	biosamples TEXT, 
	PRIMARY KEY (biosamples)
);
