/*
--------------------------------------------------------------------
Name   : Nackademin
Author : Anton L
--------------------------------------------------------------------
*/

-- Notes lägg till schemas?
-- Indexes?



-- Skapar databas för slutuppgiften
CREATE DATABASE Smakademin1;
GO

-- Växlar till ny databas
USE Smakademin1;
GO

-------------------------------------------------------------------- Skapar tabeller!

CREATE TABLE Education_location
(
	[location_id] INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	[location] VARCHAR(50) NOT NULL,
)
GO


CREATE TABLE Education_field
(
	[field_id] INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	[field] VARCHAR(50) NOT NULL,
)
GO

CREATE TABLE Education_type
(
	[type_id] INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	[type_name] VARCHAR(50) NOT NULL,
)
GO

CREATE TABLE Education_points
(
	[points_id] INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,	
	[points] INT			,
	[length_weeks] INT		, 
)
GO


CREATE TABLE Education
(
	[education_id]  INT         NOT NULL,
	[edu_name]      VARCHAR(50) NOT NULL,
	[start_date]    DATE		,
	[price]         SMALLMONEY  ,
	[type]          INT	FOREIGN KEY REFERENCES Education_type([type_id]),
	[field]         INT	FOREIGN KEY REFERENCES Education_field(field_id),
    [location]      INT	FOREIGN KEY REFERENCES Education_location(location_id),
    [points]        INT	FOREIGN KEY REFERENCES Education_points(points_id),
)
GO


CREATE TABLE Education_webcontent
(
	[title] VARCHAR(100),
	[text body] TEXT	, 
	[Education_content] INT FOREIGN KEY REFERENCES Education(education_id)
)
GO


-------------------------------------------------------------------- Insert values to edu_type

INSERT INTO Education_type
VALUES
	('Utbildning')				,
	('Kurser')					,
	('Distans')					, -- självstudier
	('Satellit')				,
	('YH-utbildning')			,
	('Preparandkurs')			,
	('YH-kurs')

INSERT INTO Education_field
VALUES
	('IT')						,
	('Bygg')					,
	('Kommunikation')			,
	('Design')					,
	('Elteknik och energi')		,
	('Vård och hälsa')

INSERT INTO Education_location
VALUES
	('Stockholm')				,
	('Distans')					, --Ortsoberoende
	('Uppsala')					,
	('Visby')					,
	('Nässjö')					,
	('Solna')


INSERT INTO Education_points
VALUES
    (600)						,
	(550)						,    
    (500)						,
	(450)						,	
    (400)						,
	(350)						,	
    (300)						,
	(250)						,	
    (200)						,
	(150)						,    
	(100)						,
    (90)						,
	(80)						,
	(70)						,
	(60)						,
	(50)						,
	(40)						,
	(30)						,
	(20)						,
	(10)                
	

INSERT INTO Utbildning (Namn, Längd, Form, Pris, Ämne, Ort, YH_poäng)
VALUES('Devops Engineer', '2 år', (select Form from Studieform where Form='Utbildning'), 0, (select Ämne from Kategori where Ämne='IT'), (select Ort from Studieort where Ort='Solna'), 
(select YH_Poäng from YH_Poäng where YH_poäng=400))

INSERT INTO Utbildning (Namn, Sista_anmälningsdag, Längd, Form, Pris, Ämne, Ort, YH_poäng)
VALUES ('Frontend-utvecklare', '2021-05-04', '2 år', (select Form from Studieform where Form='Utbildning'), 0, (select Ämne from Kategori where Ämne='IT'), (select Ort from Studieort where Ort='Solna'),
	(select YH_Poäng from YH_Poäng where YH_poäng=400))

INSERT INTO Utbildning (Namn, Kursstart, Kursslut, Sista_anmälningsdag, Längd, Form, Pris, Ämne, Ort)
VALUES ('Testautomatiserare', '2021-02-17', '2021-04-28', '2020-12-20', '10 veckor',
	(select Form from Studieform where Form='Distans'), 29500,
	(select Ämne from Kategori where Ämne='IT'), 
	(select Ort from Studieort where Ort='Distans'))


INSERT INTO Innehåll (utb_id, Rubrik, Förklaring)
VALUES ((select utb_id from Utbildning where utb_id=1), 
	'DevOps Engineer', 'DevOps Engineer är ett av IT-branschens hetaste yrken med mycket stor efterfrågan! 
	DevOps är en kombination av drifttekniker och systemutvecklare där du  deltar i hela servicelivscykeln, 
	från design av process till produktionsstödd utveckling och drifttagning. 
	Fokus för en DevOps Engineer är att höja värdet av IT-leveransen genom att skapa ett snabbt och effektivt flöde från kravspec till driftsatt tjänst. 
	Du kommer under utbildningen att få kunskaper både inom programmering och drift.
	Development Operations, eller DevOps, är den relativt nya yrkesgrupp inom IT som står mellan 
	utvecklingsavdelningens (Development) snabbföränderliga mål och visioner och systemförvaltningens (Operations) 
	ansvar för att systemen faktiskt fungerar som de ska. Det handlar om processoptimering så att utvecklingsprocesser går smidigare. 
	Om att planera och identifiera resurser för att designa infrastrukturlösningar för 
	utveckling, testning, automatisering, driftsättning och drift. En DevOps Engineer måste ha kunskap om och 
	färdigheter i de tekniker som används, från programmering till Configuration Management-verktyg samt metoder för 
	Continuous Integration och Continuous Delivery.
	Branschen är i ständig förändring och en viktig del i yrkesrollen DevOps Engineer är att optimera och effektivisera utvecklingscykeln 
	för en IT-avdelning. Du behöver därför alltid ha koll på nya metoder och de senaste teknikerna.')

INSERT INTO Innehåll (utb_id, Rubrik, Förklaring)
VALUES ((select utb_id from Utbildning where utb_id=2), 
	'Frontend-utvecklare', 
	'Som Frontend-utvecklare arbetar du med presentationslagret – 
	det man ser och använder när man surfar på en webbplats. Det gäller att skapa 
	logisk och effektiv Frontend-kod för att göra sidorna så välfungerande, 
	innovativa och funktionella som möjligt. Men de ska också fungera lika bra 
	oavsett om man använder en webbläsare, smartphone eller surfplatta. 
	Det teknologiska skiftet som sker ex. inom handeln kräver specialistkompetens som det är brist på idag. 
	Om du är intresserad av en bransch där nya metoder introduceras kontinuerligt, programmering och problemlösning – 
	då kan det här vara utbildningen för dig!')





-------------------------------------------------------------------- Lägger till procedurer




CREATE TABLE Edu_type
(
	type_of_edu VARCHAR(50) PRIMARY KEY NOT NULL
)

CREATE TABLE Edu_field
(
	edu_field VARCHAR(50) PRIMARY KEY NOT NULL
)



CREATE TABLE Edu_location
(
	location_name VARCHAR(50) PRIMARY KEY NOT NULL,
	location_country VARCHAR(50)
)

CREATE TABLE Edu_credit_units
(
	edu_type SMALLINT PRIMARY KEY NOT NULL 
)


CREATE TABLE Edu
(
	edu_id INT IDENTITY(1, 1) PRIMARY KEY NOT NULL,
	edu_name VARCHAR(50) NOT NULL,
	edu_start_date DATE,
	edu_end_date DATE,
	edu_registration_open DATE,
	edu_registration_close DATE,
	edu_price MONEY,
	edu_type VARCHAR(50) FOREIGN KEY REFERENCES Edu_type(edu_type),
	edu_location VARCHAR(50) FOREIGN KEY REFERENCES Edu_type(edu_type)
)

CREATE TABLE Edu_web_content
(
	edu_id INT FOREIGN KEY REFERENCES Edu(edu_id), --NOT NULL?
	content_titel VARCHAR(100),
	content_body TEXT,
	content_img VARBINARY

)

-- Insert values to edu_type
INSERT INTO Edu_type
VALUES ('IT'), ('Bygg'), ('Kommunikation'), ('Design'), ('Elteknik och energi'), ('Vård och hälsa'), ('Pedagogik')

-- Insert values to edu_location
INSERT INTO Edu_location (location_name)
VALUES ('Orts oberoende'), ('Stockholm'), ('Uppsala'), ('Visby'), ('Nässjö'), ('Solna')

-- Insert values to edu_credit_units
INSERT INTO Edu_credit_units VALUES
(20), (40), (60), (80), (100), (200), (400), (600)

