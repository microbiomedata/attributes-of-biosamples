

CREATE TABLE "Biosample" (
	id TEXT, 
	depth TEXT, 
	PRIMARY KEY (id, depth)
);

CREATE TABLE "BiosampleCollection" (
	biosamples TEXT, 
	PRIMARY KEY (biosamples)
);
