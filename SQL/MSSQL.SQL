-- 1.  Tabellen Employee innehåller anställda. Visa samtliga rader (alla kolumner och alla rader) som finns i tabellen Employee.
select *
from Employee

-- 2.  Visa alla rader som finns i Employee-tabellen, där den anställde har anställningsdatum lika med 2002-12-03.Obs! Skriv samma datumformat som i tabellen!
select *
from Employee
where HireDate = '2002-12-03'

-- 3.  Visa alla personer i Employee-tabellen som anställdes senare än 2000-01-01.
select *
from Employee
where HireDate > '2000-01-01'

-- 4.  Visa enbart kolumnerna efternamn (lastname), jobb (job), lön (salary) och bonus (commission) för de personer som har mer än 20000 kr i lön.
select
	Firstname,
	Lastname,
	Salary,
	Commission
from Employee
where Salary > 20000

-- 5. Visa för- och efternamn (firstname respektive lastname) och inkomst för alla säljare. Inkomsten är summan av lön (salary) och bonus (commission). Slå upp ISNULL i hjälpen om du hinner!
select
	Firstname,
	Lastname,
	Salary + isnull(Commission, 0) as 'Inkomst'
from Employee
where job = 'Säljare'

-- 6. De personer som har mindre än 10000 kr i grundlön (salary) ska eventuellt få ett lönelyft på 10%. Visa efternamn, lön och nya lönen för dessa. Benämn kolumnerna Efternamn, Lön och NyLön.
select 
	Lastname as 'Efternamn',
	Salary as 'Lön',
	Salary * 1.1 as 'Nylön'
from Employee
where Salary < 10000

-- 7. Visa hur mycket varje person ska betala i skatt. Antag att man betalar 30% i skatt. Visa Efternamn, Inkomst och Skatt.
select
	Lastname,
	Salary + isnull(Commission, 0) as 'Inkomst',
	(Salary + isnull(Commission, 0)) * 0.30 as 'Skatt'
from Employee

-- 8. Visa Efternamn, Lön, Bonus på alla anställda som inte har någon bonus.
select
	Lastname,
	Salary,
	Commission
from Employee
where
	Commission is null

-- 9. Visa Lastname, Job och Salary på alla chefer som heter JONES.
select
	Lastname,
	Job,
	Salary
from Employee
where job = 'Chef' and (firstname = 'Jones' or Lastname = 'Jones')

-- Överkurs
-- 10. Visa Lastname, Job och Salary på alla chefer som INTE heter JONES.
select
	Lastname,
	Job,
	Salary
from Employee
where job = 'Chef' and not (firstname = 'Jones' or Lastname = 'Jones')

-- 11. Visa alla rader vars efternamn börjar på ’J’ eller innehåller ’AR’.
select
	*
from Employee
where Lastname like 'J%' or lastname like '%AR%'


-- 12. Gör en e-mail-lista genom att konkatenera för- och efternamn. Formatet ska vara förnamn.efternamn@nackademin.se. Slå upp LOWER i hjälpen om du hinner!
select
	lower(replace(firstname + '.' + Lastname + '@nackademin.se', ' ', '.'))
from Employee

-- 13. Visa Efternamn, Anställningsnummer (EmpID) på alla anställda som har ett anställningsnummer mellan 7600 och 7800.
select
	Lastname,
	EmpID
from Employee
where EmpID between 7600 and 7800

-- 14. Visa alla rader för de anställda som tjänar 11.000, 28.000 eller 30.000 kr i månaden.
select
	*
from Employee
where Salary in (11000, 28000, 30000)

-- 15. Visa samtliga varianter på namn från tabellerna fotboll och ishockey. Resultatet ska vara utan dubbletter.
select
	namn
from Fotboll
union
select
	namn
from Ishockey

-- 16. Visa alla fotbolls- och ishockeyspelare inklusive dubbletter.
select
	namn
from Fotboll
union all
select
	namn
from Ishockey

-- 17. Visa vilka orter som företaget har kontor i (utan dubbletter). Tabellen är Department.
select
    distinct [Location]
from Department

-- 18. Visa namnen (namn) på alla spelare som både spelar fotboll och ishockey.
select
	namn
from Fotboll
intersect
select
	namn
from Ishockey
-- 19. Visa namnen på de spelare som bara spelar fotboll.
select
	namn
from Fotboll
except
select
	namn
from Ishockey
-- 20. Visa namnen på de spelare som bara spelar ishockey.
select
	namn
from Ishockey
except
select
	namn
from Fotboll

-- 21. Visa de avdelningar (DeptID) som har några anställda.

select *
from Department
where DeptID in
(	select DeptID
	from Employee )

-- 22. Visa de avdelningar som inte har några anställda.
select *
from Department
where DeptID not in 
(	select DeptID
	from Employee)

-- ——— NY LEKTION 
-- 1.Ange hur många anställda som har en grundlön som är mer än 25000 kr.
select
	count(*) as 'Antal anställda'
from Employee
where Salary > 25000

-- 2.Summera alla anställdas grundlöner.
select
	sum(salary)
from Employee

-- 3.Hur mycket tjänar den som tjänar mest respektive minst i företaget?
select
	max(salary) as 'Max lön',
	min(salary) as 'Min lön'
from Employee

-- 4.Ange den totala kostnaden för samtliga anställdas grundlöner om resp persons grundlön höjs med 10%. Visa även skillnaden i kronor mot den gamla lönen.
select
	sum(salary) as 'Lön idag',
	sum(salary) * 1.1 as 'Löneförhöjning',
	sum(salary) * 1.1 - sum(salary) as 'Skillnad'
from Employee

-- 5.Flytta fram anställningsdatum ett år för alla anställda. Visa det som nytt anställningsdatum i svarstabellen.
select
	EmpID,
	Firstname,
	Lastname,
	convert(varchar(10), HireDate, 120),
	convert(varchar(10), dateadd(year, 1, hiredate), 120)
from Employee

-- 7.Beräkna standardavvikelsen för lönen till alla chefer (Chef eller VD). Slå upp i hjälpen!
select
	round(stdev(Salary), 0)
from Employee
where job in ('Chef', 'VD')

-- 8.Beräkna antalet månader mellan dagens datum och de anställdas anställningsdatum i Employee.
select
	*,
	datediff(MONTH, HireDate, getdate()) as 'Månader anställd'
from Employee


-- 9.Fyll ut med understreck _ till höger om efternamn. Totala stränglängden för kolumnen ska vara 15.
--1
select
	left(lastname + '_____________', 15)
from Employee

--2 
select
	lastname + replicate('_',(15-len(lastname)))
from Employee

-- 10.Byt jobb på alla som är Kontorist till Assistent
select
	firstname,
	Lastname,
	replace(job, 'Kontorist', 'Assistent') as 'Job'
from Employee


-- 11.Skriv allas namn (lastname) med versal första bokstav, resten gemena.

select
	upper(left(lastname, 1)) + lower(right(Lastname, (len(lastname)-1)))
from Employee


-- 12.Skapa både för- och efternamn i en kolumn, och en signatur i nästa kolumn. Signaturen ska vara versaler och bestå av första två bokstäverna i förnamn resp efternamn (Göran Persson skulle få signaturen GÖPE). 


-- 13.Byt ut sista bokstaven i namnet mot en * på alla som arbetar på avdelning 30.


-- 14.Visa hur många år den som arbetat längst respektive kortast tid på företaget har arbetat.


-- 15.Visa namnet BLAKE i stället för 7698 för de som har BLAKE som chef, annars visas bara MGR. Visa ENAME, JOB, MGR. Obs! Använd CASE (i Oracle decode).


-- Överkurs


-- 16.Visa hur många dagar längre den som arbetat längst på företaget har arbetat, jämfört med den som arbetat kortast tid.


-- ——





-- 1.Visa efternamn (Lastname) och lön (Salary) på alla som arbetar som Säljare i tabellen anställda (Employee). Sortera i bokstavsordning på efternamnet


-- 2.Sortera alla efter grundlön (Salary) med den högst betalde överst. Har två eller fler samma lön ska bokstavsordning på efternamn gälla. Visa hela tabellen Employee.


-- 3.Visa alla anställda efter 2000-01-01(Hiredate), med den sist anställde överst.


-- 4.Räkna ut hur många kunder det finns på varje ort. Använd tabellen Customers.


-- 5.Visa de orter och antalet kunder där företaget har fler än 5 kunder. Visa i fallande antal-ordning.


-- 6.Visa de orter och antalet kunder där säljaren Carola Karlsson har fler än en kund. Sortera fallande efter antal. 


-- 7.Visa de orter och antalet kunder på orten som inte blivit tilldelad en säljrepresentant (dvs där EmpID är NULL).


-- 8.Visa namnen på de populäraste blommorna följt av antalet. De mest sålda blommorna ska vara överst. Använd tabellen OrderDetails.


-- 9.Det kanske inte är lönsamt att ha alla typer av blommor på lager. Visa de buketter som sålts 3 gånger eller färre.


-- 10.Visa intäkt per artikel (oavsett om det är en bukett eller frakt) med den mest inkomstbringande artikeln överst. Visa tre kolumner: artikelns namn, intäkt och antal sålda artiklar.


-- ———





-- 1.Ta reda på var alla anställda arbetar med hjälp av tabellerna Employee och Department. Visa efternamn (Lastname), lön (Salary), avdnummer (DeptID) och arbetsplats (Location). Sortera på arbetsplats och namn.


-- 2.Samma som ovan, men visa även de avdelningar som inte har några anställda.


-- 3.Samma som 1, men ta bara med de som arbetar i Stockholm.


-- 4.Vad heter avdelningen där Smith arbetar?


-- 5.Lista alla anställningsnummer (EmpID), efternamn (Lastname) och chefens anställningsnummer (ManagerID) från tabellen Employee. Använd vanlig SELECT!


-- 6.Samma som uppgift 5 men ta även med namnet för chefen (en egenkoppling på Employee-tabellen).


-- 7.Som uppgift 5 men se till att även de som inte har någon chef kommer med i listan. (Yttre koppling)


-- 8.Som uppgift 6 men lägg till kolumnerna för de anställdas  och chefernas lön. Gör en restriktion så att endast anställda som tjänar mer än sin chef kommer med.


-- 9.Ta reda på anställningsnummer och efternamn för alla chefer och räkna ut medellönen för de personer som är direkt underställd respektive chef. Visa i ett svar.


-- 10.Visa namn och jobb på som har samma arbete som CLARK.


-- 11.Vilken säljare tjänar mest inklusive provision (Commission)? Observera att det kan förekomma NULL-värden. Hantera i så fall dessa!


-- 12.Vilka anställda har BLAKE som chef?


-- 13.Vilka arbetar i samma stad som Smith?


-- 14.Visa avdelningsnamn och lönekostnad per avdelning. 


-- I lönekostnaden ingår provision.


-- 15.Samma som ovan men ta bara med de avdelningar som har fler än tre anställda. 


-- 16.Samma som ovan, men visa även avdelningsort (Location). 


-- 17.Visa anställningsdatum för den längsta respektive den kortaste tid någon har varit anställd på varje ort. 


-- ——— LEKTION 6

-- 1.Lägg till en rad med följande värden i tabellen COUNTRY
--   CountryId:  BRA Country:  BrasilienPopulation:    140000000 Government:  Demokrati

begin tran
insert into country (CountryID, Country, Population, Government)
values('BRA','Brasilien', 140000000, 'Demokrati')

rollback tran

-- 2.Lägg till Rio de Janeiro i CITY-tabellen. Rio de Janeiro har 10 miljoner invånare.

begin tran
insert into city (City, CountryId, Population)
values('Rio de Janeiro', 'BRA', 10000000)

rollback tran

-- 3.Lägg till Umeå (40000 invånare), Norrköping (115000 invånare) och Örebro (90000 invånare) utan att ange kolumnnamn i Insert-satsen.

begin tran
insert into city
values
('Umeå', 'SWE', 40000),
('Norrköping', 'SWE', 115000),
('Örebro', 'SWE', 90000)

rollback tran

-- 4.Byt ut den svenska beteckningen (COUNTRYID) mot SVE i COUNTRY- och CITY-tabellerna.

begin tran
update city
	set CountryId = 'SVE'
	where CountryId = 'SWE'
update country
	set CountryId = 'SVE'
	where CountryId = 'SWE'
rollback tran

-- 5.Det finns ett land och en stad där invånarantalet saknas. Uppdatera dessa kolumner med lämpliga (eller påhittade) värden.

begin tran
update city	
	set Population = 275524
	where CountryId = 'JUG' and city = 'Sarajevo'
update country	
	set Population = 10304827
	where CountryId = 'JUG' and country = 'Jugoslavien' and Population is null
rollback tran

-- 6.Uppdatera befolkningsmängden för alla länder och städer med 100 procent.

begin tran
update city
	set Population *= 2
update country
	set Population *= 2
rollback tran
commit tran


-- 7.Lägg till alla städer från Customers-tabellen i City-tabellen. Utgå från att alla städer som finns i Customers-tabellen finns i Sverige. Ange inget invånarantal.

begin tran
insert into city (City, CountryId)
select
	city,
	'SVE'
from Customers
rollback tran
commit tran


-- 8.Ta bort de rader som lades till ovan.
begin tran
delete from city
where Population is null

-- 9.Lägg till städer från Customers-tabellen i City-tabellen, men se till att du inte lägger in dubbletter. Undvik också att skapa dubbletter (d v s lägg inte in en stad som redan finns).

begin tran
insert city (City, CountryId)
	
	select distinct city, 'SVE'
	from Customers
	where city collate Finnish_Swedish_CI_AI not in(
	select city from city)

rollback tran
commit tran

-- 10.Sätt alla befolkningstal i Country-tabellen så att summan av befolkningen i de olika städerna utgör hela befolkningen i landet, d v s SUM(City.Population) = Country.Population för varje land. 
--GÖR OM

begin tran
update country
set Population =
(
	select sum(isnull(population, 0))
	from city
	where country.CountryId = city.CountryId
	group by CountryId
)

rollback tran

-- 11.Uppdatera lönen för alla anställda som arbetar i Stockholm med 30 %.
--GÖR OM
begin tran

update Employee
set Salary = salary * 1.3
where deptid = 
(
	select DeptID
	from Department
	where location = 'Stockholm'
)
rollback tran

-- 12.Uppdatera STEVE MILLER, så namnet är med inledande versal och resten gemener, d v s Steve Miller.
-- GÖR OM
begin tran
update Employee
	set firstname = 'Steve', lastname = 'Miller'
where EmpID = 7934
rollback tran

-- 13.Lägg till en anställd i Employee-tabellen. Valfritt namn, jobb, lön och avdelning.
begin tran
insert Employee (empid, firstname, lastname, job, Salary, DeptID)
values(1252, 'Pelle', 'Svanslös', 'CEO', 1000000, 50)
rollback tran

select * from Employee

-- 14.Ta bort alla rader i Department-tabellen. Går det? Borde det gå? Vad händer i så fall med raderna i Employee-tabellen?

begin tran


rollback tran


-- •Till sist ska vi återställa tabellerna. Det gör vi med:



select * from city


--- Skapa en tabell med namnet ANST, som är en kopia på tabellen Employee
select *
into ANST
from Employee


-- Ändra kolumnen Lastname i tabellen ANST till VARCHAR(50). Skriv kommandot SP_HELP ANST för att se tabellens engenskaper

SP_HELP ANST
select * from ANST

alter table ANST
alter column lastname varchar(50)


--- Lägg till en ny kolumn MANAGER CHAR(1) i tabellen ANST

alter table anst
add manager char(1)


-- Uppdatera tabellen ANST och sätt ett 'y' i manager-columnen fr de som har några anställda underställda sig.

update ANST
set manager = 'Y'
where EmpId in (
    select managerId
    from ANST
)

-- Uppdatera tabellen ANST och sätt ett 'N' i manager-columnen för de som INTE har några anställda underställda sig.

update ANST
set manager = 'N'
where EmpId not in (
    select managerId
    from ANST
)

-- Ändra kolumnen MANAGER i tabbellen ANST till NOT NULL.
alter table anst
alter column manager char(1) not null

-- Skapa en kopia av tabllen department, namnge den AVD
select *
into avd from Department

-- Skapa en primär nyckel på kolumnen DeptID i tabellen AVD
alter table avd
add primary key(deptid)

-- Skapa en referial integrity constraint mellan tabellerna ANST och AVD.
-- Alltså en främmande nyckel på kolymnen deptno i ANST. Namnge den FK_DEPTNUM

alter table anst
add constraint fk_deptnum foreign key (deptid)
references avd(deptid)


-- Ta bort avdelning 10 från tablellen AVD. Gick det?
delete from avd
where DeptID = 10

-- Ta bort constraint FK_DEPTNUM
alter table anst
drop constraint FK_DEPTNUM

-- Ta bort avdelning 10 från tablellen AVD. Gick det?
delete from avd
where DeptID = 10

-- Ta bort tabellerna AVD och ANST
drop table avd
drop table anst


-- skapa en tabell; totalinfo. Den ska innehålla alla kolumner från Employee och Department. Ta endast med DeptId en gång. 
-- Vilka fördelar respektive nackledar fnns det med denna enda tabell istället för två tabbeller Employee och Department=


select EmpID, Firstname, Lastname, Job, ManagerID, HireDate, Salary, Commission, e.DeptID, DeptName, Location
into totalinfo
from Employee e
inner join Department D
on e.DeptID = d.DeptID


--- NY lektion


-- 1. Skapa en vy baserad på tabellen Customers och kalla den VY1. Ta med kolumnerna Cust_ID, Firstname, Lastname, City och sätt egna namn på kolumnerna.  
go
create view VY1 (Kundnr, Förnamn, Efternamn, Stad) as
	select
		Cust_ID,
		FirstName,
		LastName,
		city
	from Customers
go

-- 2. Gör en vy av Employee- och Department-tabellerna och kalla den VY2. Den ska innehålla alla anställda som tjänar mer än 10 000. Ta med kolumnerna anställningsnr, efternamn, jobb, lön och avdelningsnamn.
go
create view VY2 (Anställningsnr, Efternamn, Jobb, Lön, avdelningsnamn) as
	select
		EmpID,
		Lastname,
		Job,
		Salary,
		d.DeptName
	from Employee e
	join Department d
	on e.DeptID = d.DeptID
	where Salary > 10000
go
-- 3. Skapa VY3 baserad på VY2 där lönen är omvandlad till dollar. En dollar är värd 7.50 skr.
go
create view VY3 as
	select
		Anställningsnr,
		Efternamn,
		Jobb,
		cast(Lön / 7.5 as int) as 'Lön i dollar',
		avdelningsnamn
	from VY2
go
-- 4. Ta bort vyerna VY1, VY2 och VY3.
drop view VY1, VY2, VY3

-- 5. Skapa en vy VY5 av Employee-tabellen där man slår ihop Lön (salary) och Bonus (commission) till en kolumn. Ta med efternamn, jobb och den nya lönekolumnen.
go
create view vy5 as
	select 
		Lastname,
		job,
		Salary + isnull(commission, 0) as 'Nylön'
	from Employee


-- 6. Se till att de som inte har någon bonus ändå får med sin lön i den nya kolumnen.
go
create view VY6 as
	select 
		Lastname,
		job,
		Salary + isnull(commission, 0) as 'Nylön'
	from Employee

-- 7 .Samma som ovan men lägg till en kolumn som visar varje anställds chef. De som inte har någon chef får texten ’The Boss’ i stället.
go
create view VY7 as
	select 
		w.Lastname,
		w.job,
		w.Salary + isnull(w.commission, 0) as 'Nylön',
		isnull(m.Lastname, 'The Boss') as 'Chef'
	from Employee w join Employee m
	on w.ManagerID = m.EmpID
go
-- 8. Skapa en vy som visar avdelning, plats, antal anställda, medellönen och maxlönen för varje avdelning. 
go
create view VY8 (Avd, plats, antal, medelön, maxlön) as
	select 
		DeptName,
		Location,
		count(Lastname),
		avg(Salary),
		max(Salary)
	from Employee e join Department d
	on e.DeptID = d.DeptID
	group by DeptName, Location
go


-- 9. Skapa en vy som talar om vad varje anställd ska betala i skatt varje månad. Antag att man betalar 30% i skatt. Ta med kolumnerna Namn(lastname) och skatt. De som har bonus (comm) ska betala 50% i skatt på sin bonus men bara 30% på lönen.
go
create view VY9 as
	select
		lastname as 'Namn',
		salary * 0.3 + isnull(Commission, 0) * 0.5 as 'Skatt'
	from Employee
go
-- 10. Ta bort alla vyer
drop view VY1, VY2, VY3, VY4, VY5, VY6, VY7, VY8, VY9


-- 11. Skapa en chefs-vy, enbart bestående av chefer, deras anställningsnummer, lön, jobbtitel, för- och efternamn samt orten där de arbetar.
go
create view chefsvy as
	select
		EmpID
		Salary,
		job,
		firstname,
		lastname,
		Location
	from Employee e join Department d
	on e.DeptID = d.DeptID
	where e.EmpID in 
	(
		select
			distinct ManagerID
		from Employee
	)
go

-----------------------------

-- 1. Se till att tabellen Employee blir indexerad på lön, med högsta lönen först.

create index idx_employee_salary on Employee (Salary desc)

select
	 Salary
from Employee

-- 2. Ta bort ovanstpende index.

drop index Employee.idx_employee_salary


-- 3. Skapa en kopia på Department och döp den till Dept. Ska därefter ett unikt sammansatt index på kolumnerna Deptname och Location i tabellen Dept.
--    Försök ändra namn till Ekonomi där DeptID = 10.

select * into Dept from Department

create unique index udx_DeptLoc on dept(deptname, location)

update dept
set DeptName = 'Ekonimi'
where DeptID=10

select *
from Dept

-- 4. Ta bort tabellen Dept. Försvinner det index som du skapade automatiskt när tabellen tas bort?
-- Svar ja!

select * from sysindexes
where name = 'dept'


----- NY LEKTION

-- 1. Skapa en procedur som har en input parameter. Denna parameter ska representera Name.
-- Om man anropar proceduren utan att ange parametern ska returvärdet vara samtliga personer i Employee.
-- Om man anropar proceduren med värdet på parametern till A ska returvärdet vara de som har ett för- eller efternamn som startar på A.
-- Anger man AN ska returvärdet vara de som har ett för- eller efternamn som startar på AN etc.

declare @name varchar(10)
	set @name = 's%'
go
create proc usp_Search (@name varchar(50) = '%') as
begin
	select * from Employee
	where
	lastname like @name or
	firstname like @name
end
go
usp_search '%'


-- 2. Ändra tabellen Employee, och lägg till kolumner för Username och Password. Försök använda Alter table-kommandot. 
alter table employee
add username varchar(10)

alter table employee
add password varchar(10)

select *
from Employee

-- 3.Uppdatera några användare och ge dem lämpliga Username och Password. Försök använda Update-kommandot. 
update Employee
set password = 'hemligt'

update Employee
set username = LEFT(Firstname, 3) + LEFT(Lastname, 3)


-- 4. Skapa en procedur som har två input parametrar; en för Username och Password. När man anropar proceduren och dessa Username + password är korrekt, ska returvärdet vara EmpID.
-- Är det fel ska returvärdet vara ”Wrong username” resp ”Wrong password”. 


drop proc usp_pwdCheck
go

create proc usp_pwdCheck (@username varchar(10), @pwd varchar(10))
as 
begin


	--deklarera variabler
    declare @FoundUsername varchar(10)
    declare @FoundPwd varchar(10)
    declare @EmpID int


    --tilldela värden
    select 
        @EmpID = EmpID,
        @FoundUsername = username,
        @FoundPwd = password
    from Employee
    where username = @username

--debug
select @EmpID, @FoundUsername, @FoundPwd

    --användare hittas inte
    if @FoundUsername is null
    begin
        select 'Wrong username' as Returnvalue
        return
    end

	-- användare finns, kolla lösenord
	if @FoundPwd = @pwd
		select @EmpID as Returnvalue
	else
		select 'Bad Password' as Returnvalue



end
go

usp_pwdCheck 'andcar', 'hemligt'



----- 


-- 1.   Skapa en transaktion. Gör en uppdatering på innehållet i valfri tabell.

-- 2.   Skapa en savepoint. Gör en uppdatering till. Skapa en ny savepoint.
--      Gör ytterligare en uppdatering. Kontrollera uppdateringarna.

-- 3.   Backa uppdateringen tillbaks till den andra savepointen. Kontrollera värdena.
--      Gå tillbaks till första savepointen. Vad händer med andra savepointen?

-- 4.   Gör om övning 1-2 men gör en commit efter andra uppdateringen. 
--      Försök gå tillbaka till savepoint-läget.

-- 5.   Ta bort alla rader i någon tabell. Boot:a om datorn (simulera krasch).
--      Logga in mot databasen på nytt och kontrollera den tömda tabellen.

-- 6.   Starta två fönster i Management Studio. Starta transaktioner i bägge sessionerna.
--      Ta bort innehållet i tabellen ISHOCKEY i den ena sessionen.
--      Växla till session 2 och sök ut alla rader i ISHOCKEY-tabellen. Bekräfta
--      raderingen i den första sessionen med Commit och gör om sökningen i session 2.

-- 7.   Starta transaktioner i bägge sessionerna. Ta bort en rad i FOTBOLL-tabellen i
--      session 1. Försök uppdatera samma rad i session 2.
--      Gå tillbaks till session 1 och bekräfta borttagningen.

-- Överkurs
-- 8.   Starta två fönster i Management Studio. Starta en transaktion och ta bort alla
--      rader från tabellen Employee i den ena sessionen. Växla till det andra fönstret
--      och sök ut alla rader i Employee-tabellen. 
    --      Fönster 2 borde inte få något resultat.


-- 9.   Starta ytterligare ett fönster i Management Studio. Skriv sp_lock för att se 
--      låsningen. I kolumnen spid ser man vilken koppling som låser, exempelvis SPID 52.
    --      ”Döda” den process som orsakar låsningen genom KILL 52.
    --      Alla transaktioner i en dödad process kommer att rullas tillbaks. 
    --      Fönster 2 borde få sitt resultat nu.