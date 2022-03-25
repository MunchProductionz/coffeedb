BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Bruker" (
	"BrukerID"	INTEGER,
	"Epostadresse"	TEXT UNIQUE,
	"Passord"	TEXT NOT NULL,
	"Fulltnavn"	TEXT NOT NULL,
	PRIMARY KEY("BrukerID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Brenneri" (
	"Navn"	TEXT,
	"Sted"	TEXT,
	PRIMARY KEY("Navn")
);
CREATE TABLE IF NOT EXISTS "Gård" (
	"GårdID"	INTEGER,
	"Navn"	TEXT,
	"Høyde"	TEXT,
	"Region"	TEXT NOT NULL,
	"Land"	TEXT NOT NULL,
	PRIMARY KEY("GårdID")
);
CREATE TABLE IF NOT EXISTS "Kaffebønne" (
	"Sort"	TEXT,
	"Art"	TEXT NOT NULL,
	PRIMARY KEY("Sort")
);
CREATE TABLE IF NOT EXISTS "Foredlingsmetode" (
	"Navn"	TEXT,
	"Beskrivelse"	TEXT,
	PRIMARY KEY("Navn")
);
CREATE TABLE IF NOT EXISTS "Kaffeparti" (
	"PartiID"	INTEGER,
	"Innhøstingsår"	YEAR,
	"KiloprisUSD"	INTEGER,
	"Foredlingsmetode"	TEXT NOT NULL,
	"GårdID"	INTEGER NOT NULL,
	FOREIGN KEY("GårdID") REFERENCES "Gård"("GårdID"),
	FOREIGN KEY("Foredlingsmetode") REFERENCES "Foredlingsmetode"("Navn"),
	PRIMARY KEY("PartiID")
);
CREATE TABLE IF NOT EXISTS "Kaffe" (
	"Brennerinavn"	TEXT,
	"Navn"	TEXT,
	"Brenningsgrad"	TEXT NOT NULL,
	"Brenningsdato"	DATE NOT NULL,
	"Beskrivelse"	TEXT,
	"KiloprisNOK"	INTEGER,
	"PartiID"	INTEGER NOT NULL,
	FOREIGN KEY("PartiID") REFERENCES "Kaffeparti"("PartiID"),
	FOREIGN KEY("Brennerinavn") REFERENCES "Brenneri"("Navn"),
	PRIMARY KEY("Brennerinavn","Navn")
);
CREATE TABLE IF NOT EXISTS "Kaffesmaking" (
	"KaffesmakingID"	INTEGER,
	"Smaksnotat"	TEXT,
	"Poeng"	INTEGER NOT NULL,
	"Dato"	DATE,
	"BrukerID"	INTEGER,
	"Kaffenavn"	TEXT,
	"Brenneri"	TEXT,
	FOREIGN KEY("Kaffenavn") REFERENCES "Kaffe"("Navn"),
	FOREIGN KEY("BrukerID") REFERENCES "Bruker"("BrukerID"),
	FOREIGN KEY("Brenneri") REFERENCES "Brenneri"("Brennerinavn"),
	PRIMARY KEY("KaffesmakingID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "DyrkesAv" (
	"GårdID"	INTEGER,
	"Bønnesort"	TEXT,
	FOREIGN KEY("Bønnesort") REFERENCES "Kaffebønne"("Sort"),
	FOREIGN KEY("GårdID") REFERENCES "Gård"("GårdID")
);
CREATE TABLE IF NOT EXISTS "DelAvParti" (
	"PartiID"	INTEGER,
	"Bønnesort"	TEXT,
	FOREIGN KEY("PartiID") REFERENCES "Kaffeparti"("PartiID"),
	FOREIGN KEY("Bønnesort") REFERENCES "Kaffebønne"("Sort")
);
INSERT INTO "Bruker" VALUES (1,'bruker1@mail.com','123','Bruker 1');
INSERT INTO "Bruker" VALUES (2,'bruker2@mail.com','456','Bruker 2');
INSERT INTO "Bruker" VALUES (3,'bruker3@mail.com','789','Bruker 3');
INSERT INTO "Bruker" VALUES (4,'bruker4@mail.com','111','Bruker 4');
INSERT INTO "Bruker" VALUES (5,'h@bo.no','Testing123','Henrik Bø');
INSERT INTO "Brenneri" VALUES ('Bergen Brenneri','Bergen');
INSERT INTO "Brenneri" VALUES ('Oslo Brenneri','Oslo');
INSERT INTO "Brenneri" VALUES ('Trondheim Brenneri','Trondheim');
INSERT INTO "Brenneri" VALUES ('Jacobsen & Svart','Trondheim');
INSERT INTO "Gård" VALUES (1,'Sagmo Gård','1000','Bergen','Colombia');
INSERT INTO "Gård" VALUES (2,'Storvik Gård','2000','Oslo','Norge');
INSERT INTO "Gård" VALUES (3,'Bø Gård','3000','Trondheim','Rwanda');
INSERT INTO "Gård" VALUES (4,'Nombre de Dios','1500','Santa Ana','El Salvador');
INSERT INTO "Kaffebønne" VALUES ('Magnum','coffee arabica');
INSERT INTO "Kaffebønne" VALUES ('Mocca','coffee robusta');
INSERT INTO "Kaffebønne" VALUES ('Royal','coffee liberica');
INSERT INTO "Kaffebønne" VALUES ('Bourbon','coffee arabica');
INSERT INTO "Foredlingsmetode" VALUES ('Bærtørket','Hengt til tørk');
INSERT INTO "Foredlingsmetode" VALUES ('Vasket','Skylt i rist');
INSERT INTO "Foredlingsmetode" VALUES ('Plukket','Hentet rett fra plantene');
INSERT INTO "Kaffeparti" VALUES (1,2020,10,'Bærtørket',1);
INSERT INTO "Kaffeparti" VALUES (2,2021,20,'Vasket',2);
INSERT INTO "Kaffeparti" VALUES (3,2022,30,'Plukket',3);
INSERT INTO "Kaffeparti" VALUES (4,2021,8,'Bærtørket',4);
INSERT INTO "Kaffe" VALUES ('Bergen Brenneri','Nescafe','mørk','2022-01-01','Helt ok',100,1);
INSERT INTO "Kaffe" VALUES ('Oslo Brenneri','Espresso','middels','2022-02-02','Middels god',200,2);
INSERT INTO "Kaffe" VALUES ('Trondheim Brenneri','Evergood','lys','2022-03-03','Ganske god, med en floral smak',300,3);
INSERT INTO "Kaffe" VALUES ('Jacobsen & Svart','Vinterkaffe 2022','lys','2022-01-20','En velsmakende og kompleks kaffe for mørketiden',600,4);
INSERT INTO "Kaffesmaking" VALUES (1,'Grei kvalitet',3,'2022-01-02',1,'Nescafe','Bergen Brenneri');
INSERT INTO "Kaffesmaking" VALUES (2,'Smakfulle bønner',6,'2022-02-03',2,'Espresso','Oslo Brenneri');
INSERT INTO "Kaffesmaking" VALUES (3,'Gode bønner',4,'2022-02-03',2,'Espresso','Oslo Brenneri');
INSERT INTO "Kaffesmaking" VALUES (4,'Ganske grei kvalitet',5,'2022-02-03',2,'Nescafe','Bergen Brenneri');
INSERT INTO "Kaffesmaking" VALUES (5,'Bemerkelsesverdig smak',9,'2021-03-04',3,'Evergood','Trondheim Brenneri');
INSERT INTO "Kaffesmaking" VALUES (6,'Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!',10,'2022-03-21',4,'Vinterkaffe 2022','Jacobsen & Svart');
INSERT INTO "Kaffesmaking" VALUES (7,'Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!',10,'2022-03-25',5,'Vinterkaffe 2022','Jacobsen & Svart');
INSERT INTO "DyrkesAv" VALUES (1,'Magnum');
INSERT INTO "DyrkesAv" VALUES (2,'Mocca');
INSERT INTO "DyrkesAv" VALUES (3,'Royal');
INSERT INTO "DelAvParti" VALUES (1,'Magnum');
INSERT INTO "DelAvParti" VALUES (2,'Mocca');
INSERT INTO "DelAvParti" VALUES (3,'Royal');
COMMIT;
