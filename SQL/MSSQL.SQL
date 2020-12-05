/*
--------------------------------------------------------------------
Name   : Nackademin
Author : Anton L
--------------------------------------------------------------------
*/

-- Notes lägg till schemas?
-- Indexes?

-------------------------------------------------------------------- Skapar databas för slutuppgiften
CREATE DATABASE Smakademin1;
GO

-------------------------------------------------------------------- Växlar till ny databas
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
	[type] VARCHAR(50) NOT NULL,
)
GO

CREATE TABLE Education_points
(
	[points_id] INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,	
	[points] INT			,
)
GO


CREATE TABLE Education
(
	[education_id]  INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
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
	[body_text] TEXT	, 
	[Education_content] INT FOREIGN KEY REFERENCES Education(education_id)
)
GO

-------------------------------------------------------------------- Inserting data into [Education_type]

INSERT INTO Education_type
VALUES
	('Utbildning')				,
	('Kurser')					,
	('Självstudier')			,
	('Satellit')				,
	('YH-utbildning')			,
	('Preparandkurs')			,
	('YH-kurs')


-------------------------------------------------------------------- Inserting data into [Education_field]

INSERT INTO Education_field
VALUES
	('IT')						,
	('Bygg')					,
	('Kommunikation')			,
	('Design')					,
	('Elteknik och energi')		,
	('Vård och hälsa')

-------------------------------------------------------------------- Inserting data into [Education_location]

INSERT INTO Education_location
VALUES
	('Stockholm')				,
	('Ortsoberoende')			, 
	('Uppsala')					,
	('Visby')					,
	('Nässjö')					,
	('Solna')

-------------------------------------------------------------------- Inserting data into [Education_points]

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
	(10)                		,
	(0)

-------------------------------------------------------------------- Inserting data into [Education]



INSERT INTO Education ([edu_name], [price] , [location], [field], [type], [points])
VALUES('Devops Engineer', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='IT'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))

INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Frontend-utvecklare', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='IT'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Business Intelligence-analytiker', 0,
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='IT'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Arbetsledare bygg och anläggning', 0, 
	(SELECT location_id FROM Education_location WHERE location='Visby'), 
	(SELECT field_id FROM Education_field WHERE field='Bygg'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='Satellit'),
	(SELECT points_id FROM Education_points WHERE points=300))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Arbetsledare bygg och anläggning', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='Bygg'), 
	(SELECT [type_id][type_id] FROM Education_type WHERE [type]='Satellit'),
	(SELECT points_id FROM Education_points WHERE points=300))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Byggnadsingenjör BIM', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='Bygg'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Byggnadsingenjör Produktion', 0, 
	(SELECT location_id FROM Education_location WHERE location='Ortsoberoende'), 
	(SELECT field_id FROM Education_field WHERE field='Bygg'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='Självstudier'),
	(SELECT points_id FROM Education_points WHERE points=400))

INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Förpackningsutvecklare/- designer', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='Design'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Social Media Manager', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='Kommunikation'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=310))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Digital Marketing/Growth Manager', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='Kommunikation'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Social Media Manager', 0, 
	(SELECT location_id FROM Education_location WHERE location='Ortsoberoende'), 
	(SELECT field_id FROM Education_field WHERE field='Kommunikation'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='Självstudier'),
	(SELECT points_id FROM Education_points WHERE points=310))


INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('UX-designer', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='Design'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))

INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Energiingenjör', 0, 
	(SELECT location_id FROM Education_location WHERE location='Ortsoberoende'), 
	(SELECT field_id FROM Education_field WHERE field='Elteknik och energi'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='Självstudier'),
	(SELECT points_id FROM Education_points WHERE points=400))

INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Elingenjör konstruktion', 0, 
	(SELECT location_id FROM Education_location WHERE location='Solna'), 
	(SELECT field_id FROM Education_field WHERE field='Elteknik och energi'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='YH-utbildning'),
	(SELECT points_id FROM Education_points WHERE points=400))

INSERT INTO Education ([edu_name], [price], [location], [field], [type], [points])
VALUES('Tandsköterska', 65000, 
	(SELECT location_id FROM Education_location WHERE location='Ortsoberoende'), 
	(SELECT field_id FROM Education_field WHERE field='Vård och hälsa'), 
	(SELECT [type_id] FROM Education_type WHERE [type]='Självstudier'),
	(SELECT points_id FROM Education_points WHERE points=0))

-------------------------------------------------------------------- Inserting data into [Webcontent]



INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig inom devops – development + operation', 
	'DevOps Engineer är ett av IT-branschens hetaste yrken med mycket stor efterfrågan! 
	DevOps är en kombination av drifttekniker och systemutvecklare där du  deltar i hela servicelivscykeln, 
	från design av process till produktionsstödd utveckling och drifttagning. 
	Fokus för en DevOps Engineer är att höja värdet av IT-leveransen genom att 
	skapa ett snabbt och effektivt flöde från kravspec till driftsatt tjänst. 
	Du kommer under utbildningen att få kunskaper både inom programmering och drift.',
	(SELECT education_id from Education WHERE education_id=1))


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig inom frontend-utveckling',
	'Som Frontend-utvecklare arbetar du med presentationslagret – det man ser och använder när man surfar på en webbplats. 
	Det gäller att skapa logisk och effektiv Frontend-kod för att göra sidorna så välfungerande, innovativa och funktionella som möjligt. 
	Men de ska också fungera lika bra oavsett om man använder en webbläsare, smartphone eller surfplatta. 
	Det teknologiska skiftet som sker ex. inom handeln kräver specialistkompetens som det är brist på idag. 
	Om du är intresserad av en bransch där nya metoder introduceras kontinuerligt, programmering och problemlösning – då kan det här vara utbildningen för dig!',
	(SELECT education_id from Education WHERE education_id=2))


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig inom Business Intelligence inom IT',
	'Business Intelligence är ett samlingsbegrepp för olika funktioner som utvinner, hanterar och analyserar stora mängder data. 
	Som Business Intelligence-analytiker skapar du kvalificerade underlag för strategiska och taktiska affärsbeslut baserat på den insamlade datan. 
	Det handlar om att leverera rätt information till rätt person, i rätt tid. Ju mer marknaden rör sig desto snabbare och mer exakta analyser behövs.',
	(SELECT education_id from Education WHERE education_id=3))

INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig till arbetsledare!',
	'Är du spindeln i nätet som älskar att driva projekt framåt? 
	Är du organiserad och tycker om att arbeta med människor? 
	En arbetsledare inom bygg och anläggning är länken mellan platschef och yrkesarbetare, 
	och samordnar arbetet under ett projekt! Utbildningen är en satellitutbildning som kan läsas i Solna eller Visby.',
	(SELECT education_id FROM Education WHERE education_id=4)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig till arbetsledare!',
	'Är du spindeln i nätet som älskar att driva projekt framåt? 
	Är du organiserad och tycker om att arbeta med människor? 
	En arbetsledare inom bygg och anläggning är länken mellan platschef och yrkesarbetare, 
	och samordnar arbetet under ett projekt! Utbildningen är en satellitutbildning som kan läsas i Solna eller Visby.',
	(SELECT education_id FROM Education WHERE education_id=5)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig till byggnadsingenjör med inriktning mot BIM.',
	'Hur kommer byggnaden att se ut när den är klar? Kommer köket att få tillräckligt med solljus? 
	Är det någon risk att taket kollapsar av blötsnö? Dessa frågor och många fler kan besvaras innan första spadtaget, med en BIM-modell. 
	Det handlar om att skapa virtuella prototyper i 3D 4D 5D, vilket gör det möjligt att visualisera, granska och utvärdera byggprojekt redan på planeringsstadiet. 
	Den här moderna arbetsmetoden håller nu snabbt på att ta över i och förändra hela branschen.',
	(SELECT education_id FROM Education WHERE education_id=6)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig till byggnadsingenjör med inriktning mot produktion (Ortsoberoendeutbildning).',
	'Byggnadsingenjör Produktion är en Ortsoberoendeutbildning för dig som vill arbeta med nyproduktion inom bygg. 
	Är du intresserad av att vara med och bygga nya hus? Är du samtidigt en initiativrik men också en ödmjuk innovatör och lagspelare? 
	Då kan det här vara utbildningen för dig!',
	(SELECT education_id FROM Education WHERE education_id=7)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig inom digital kommunikation.',
	'I takt med den digitala utvecklingen blir vikten av att skapa och analysera digitala kampanjer, 
	aktiviteter och kanaler allt viktigare för alla typer av företag och organisationer. 
	Därför har en Digital Marketing/Growth Manager en nyckelroll inom marknadsföring, 
	analys och strategi och är specialiserad på att förstå de digitala kanalerna, 
	samordna dessa för både extern och intern kommunikation samt utforska möjligheter inom digitala affärer. 
	Utbildningen ger dig kompetens för att självständigt arbeta som Digital Marketing/Growth Manager i 
	syfte att främja din egen fortsatta lärandeprocess och följa områdets utveckling i takt med att samhället digitaliseras.',
	(SELECT education_id FROM Education WHERE education_id=8)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Social Media Manager (f.d. Digital kommunikatör i sociala medier)',
	'Idag är sociala medier en av företagens viktigaste kommunikationskanaler. 
	De är ständigt närvarande, oftast bara ett tryck bort med mobilen. 
	Det sätter krav på hur kanalerna används och är utformade vilket idag är avgörande för bilden företagen förmedlar. 
	Information och budskap sprids snabbt, vilket öppnar för stora möjligheter om mediet används på rätt vis',
	(SELECT education_id FROM Education WHERE education_id=9)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Social Media Manager - Ortsoberoende (f.d. Digital kommunikatör i sociala medier - Ortsoberoende)',
	'Idag är sociala medier en av företagens viktigaste kommunikationskanaler. 
	De är ständigt närvarande, oftast bara ett tryck bort med mobilen. 
	Det sätter krav på hur kanalerna används och är utformade vilket idag är avgörande för bilden företagen förmedlar. 
	Information och budskap sprids snabbt, vilket öppnar för stora möjligheter om mediet används på rätt vis',
	(SELECT education_id FROM Education WHERE education_id=10)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig inom förpackningsutveckling',
	'Är du en kreativ, praktisk och tekniskt lagd person, intresserad av formgivning, konstruktion, teknik och marknadsföring? 
	Då kanske du vill bli en professionell förpackningsdesigner? 
	Genom utbildningen Förpackningsutvecklare/-designer får du kompetens att utveckla förpackningskoncept med helhetsperspektiv: 
	säljande, effektiva, miljöanpassade, transportanpassade, lättöppnade och lätta att återvinna.',
	(SELECT education_id FROM Education WHERE education_id=11)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig inom UX-design',
	'UX står för User eXperience och handlar om interaktionen mellan en användare och en produkt eller tjänst. 
	Det kan gälla digitala appar för mobiltelefoner och webbtjänster, men även fysiska produkter. 
	En UX–Designers roll är att förstå sig på användaren genom olika väletablerade metoder, 
	där slutmålet är att tillsammans med utvecklare kunna skapa användarvänliga produkter.',
	(SELECT education_id FROM Education WHERE education_id=12)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig till Elingenjör med fokus på konstruktion',
	'Är du intresserad av modern teknik och smarta lösningar? 
	Gillar du tanken på att väcka liv i en hel byggnad; skapa förutsättningar för värme, ljus och kontakt mellan människor? 
	Som Elingenjör konstruktion är det du som gör ritningarna för all elektronik som ska dras och monteras i en byggnad – 
	som belysning, datanät och elinstallationer. 
	Det kan gälla bostadshus, kontor, industrimiljöer eller andra ny-, till- och ombyggnationer som behöver avancerad teknik. 
	Du blir nyckelpersonen genom hela processen, från ritning till färdig produktion!',
	(SELECT education_id FROM Education WHERE education_id=13)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig till Energiingenjör',
	'Vill du vara med och bidra till en hållbar samhällsutveckling genom att minska energiförbrukningen inom industri och fastigheter? 
	Vill du fördjupa dig inom energi-, teknik- och klimatfrågor – och dessutom jobba med att hitta nya 
	och utveckla befintliga energieffektiva lösningar utifrån miljövänlighet och kostnadseffektivitet? 
	Då är utbildningen Energiingenjör något för dig!',
	(SELECT education_id FROM Education WHERE education_id=14)
)


INSERT INTO Education_webcontent([title], [body_text], [Education_content])
VALUES('Utbilda dig till tandsköterska på  Ortsoberoende under 1 år',
	'Har du drömt om att jobba inom vård och hälsa? Funderar du på att byta karriär och vill satsa på ett stimulerande jobb? 
	Vill du ha varierande och intressanta arbetsuppgifter? 
	Det finns behov av fler tandsköterskor i stora delar av landet! 
	Ta chansen att utbilda dig till tandsköterska på Ortsoberoende hos oss på Nackademin – på bara 1 år!',
	(SELECT education_id FROM Education WHERE education_id=15)
)



-------------------------------------------------------------------- Lägger till procedurer

-- Skapar proc för ta fram utbildningarna

GO
CREATE PROC Educations
AS
SELECT
	e.edu_name AS	'Utbildning',
	l.location AS	'Plats'		,
	e.start_date	'Kursstart'	
FROM Education e
JOIN Education_location l
ON e.location = l.location_id
ORDER BY e.edu_name, l.location
GO


-- Skapar proc för specifik utbildning och plats

CREATE PROC Education_search
	@Education VARCHAR(50),
	@Location VARCHAR(50)
AS
SELECT
	e.edu_name AS	'Utbildning',
	l.location AS	'Plats'		,
	e.start_date	'Kursstart'	
FROM Education e
JOIN Education_location l
ON e.location = l.location_id
WHERE
	e.edu_name = @Education AND
	l.location = @Location
ORDER BY e.edu_name, l.location
GO




select *
from Education

select *
from Education_points

select *
from Education_location

select *
from Education_field	

select *
from Education_webcontent

select *
from Education_type

