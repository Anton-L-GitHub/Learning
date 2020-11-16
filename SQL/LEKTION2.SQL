--- 1 ----
SELECT *
FROM Employee

--- 2 ----
SELECT *
FROM Employee
WHERE HireDate = '2002-12-03'

--- 3 ----
SELECT *
FROM Employee
WHERE HireDate > '2000-01-01'

--- 4 ----
SELECT
    Lastname 'Efternamn',
    Job 'Jobb',
    Salary 'Lön',
    Commission 'Bonus'
FROM Employee
WHERE
    Salary > 20000

--- 5 ----
SELECT 
    Firstname,
    Lastname,
    Salary + isnull(Commission, 0) 'Inkomst'
FROM Employee
WHERE
    Job = 'Säljare'

--- 6 ---

SELECT
    Lastname 'Efternamn',
    Salary 'Lön',
    cast(Salary * 1.1 AS INT) 'Ny Lön'
FROM Employee
WHERE
    Salary < 10000

--- 7 ---
SELECT
    Lastname,
    Salary + isnull(Commission, 0) 'Inkomst',
    (Salary + isnull(Commission, 0)) * 0.3 'Skatt'
FROM Employee

--- 8 ---
SELECT
    Lastname,
    Salary,
    Commission
FROM Employee
WHERE
    Commission IS NULL

--- 9 ---
SELECT
    Lastname,
    Job,
    Salary
FROM Employee
WHERE
    Job = 'Chef' AND
    (Firstname = 'JONES' OR
    Lastname = 'JONES')

--- 10 ---
SELECT
    Lastname,
    Job,
    Salary
FROM Employee
WHERE
    Job = 'Chef' AND NOT
    (Firstname = 'JONES' OR
    Lastname = 'JONES')

--- 11 ---
SELECT *
FROM Employee
WHERE
    Lastname LIKE 'J%' or
    Lastname LIKE '%ar%'

--- 12 ---
SELECT
    replace(lower(Firstname + '.' + Lastname + '@nackademin.se'), ' ', '') AS email
FROM Employee

--- 13 ---
SELECT
    Lastname,
    EmpID
FROM Employee
WHERE
    EmpID BETWEEN 7600 and 7800

--- 14 ---
SELECT *
FROM
    Employee
WHERE
    Salary IN (11000, 28000, 30000) 

--- 15 ---
SELECT
    Namn
FROM Ishockey
UNION
SELECT
    Namn
FROM Ishockey

--- 16 ---

SELECT
    Namn
FROM Ishockey
UNION ALL
SELECT
    Namn
FROM Ishockey

--- 17 ---

SELECT
    distinct [Location]
FROM Department

--- 18 ---

SELECT
    Namn
FROM Ishockey
INTERSECT
SELECT
    Namn
FROM Fotboll

--- 19 ---
SELECT
    Namn
FROM Fotboll
EXCEPT
SELECT
    Namn
FROM Ishockey

--- 20 ---
SELECT
    Namn
FROM Ishockey
EXCEPT
SELECT
    Namn
FROM Fotboll

--- 21 ---
SELECT DeptID FROM Employee
INTERSECT
SELECT DeptID FROM Department

--- 22 ---
SELECT DeptID FROM Department
EXCEPT
SELECT DeptID FROM Employee

--- 23 ---
SELECT Count(*)
FROM Employee
WHERE Salary > 25000


--- 24 ---
select sum(salary)
from Employee

--- 25 ---
select
	max(salary) as 'Max lön',
	min(salary) as 'Min lön'
from Employee

--- 26 ---
select
	sum(salary) as 'Lön nu',
	sum(salary * 1.10) as 'Lön efter',
	sum(salary * 1.10) - sum(salary) as 'Skillnad'
from Employee

--- 27 ---
select
	firstname as 'Person',
	HireDate as 'Anställd datum',
	dateadd(year, 1, Hiredate) as 'Nytt datum'
from Employee

--- 27 ---
select
	firstname as 'Person',
	HireDate as 'Anställd datum',
	dateadd(year, 1, Hiredate) as 'Nytt datum'
from Employee

--- 28 ---
select
    round(stdev(salary), 0) as 'Standardavvikelsen'
from Employee
where
	job in ('Chef', 'VD')

--- 29 ---
select
	firstname as 'Person',
	HireDate as 'Anställd datum',
	datediff(month, Hiredate, getdate()) as 'Månader anställd'
from Employee


-- Visa efternamn (Lastname) och lön (Salary) på alla som arbetar som Säljare i tabellen anställda (Employee). Sortera i bokstavsordning på efternamnet
select
	lastname,
	salary
from Employee
where job = 'Säljare'
order by Lastname, Firstname

-- Sortera alla efter grundlön (Salary) med den högst betalde överst. Har två eller fler samma lön ska bokstavsordning på efternamn gälla. Visa hela tabellen Employee.
select *
from Employee
order by Salary desc, Lastname

-- Visa alla anställda efter 2000-01-01(Hiredate), med den sist anställde överst.
select 
	firstname,
	Lastname,
	HireDate
from Employee
where Hiredate > '2000-01-01'
order by HireDate desc

-- Räkna ut hur många kunder det finns på varje ort. Använd tabellen Customers.
select
	City,
	count(*)
from customers
group by City


-- Visa de orter och antalet kunder där företaget har fler än 5 kunder. Visa i fallande antal-ordning.
select
	City,
	count(*) as 'Antal kunder'
from customers
group by City
having count(*) > 5
order by [Antal kunder] desc, city

-- Visa de orter och antalet kunder där säljaren Carola Karlsson har fler än en kund. Sortera fallande efter antal. 
select
	City,
	count(*) as 'Antal kunder'
from Customers
where EmpID = '8125'
group by City
order by [Antal kunder] desc, City

-- Visa de orter och antalet kunder på orten som inte blivit tilldelad en säljrepresentant (dvs där EmpID är NULL).
select
	City,
	count(city) as 'Antal kunder'
from Customers
where EmpID is null
group by City
order by [Antal kunder] desc, city

-- Visa namnen på de populäraste blommorna följt av antalet. De mest sålda blommorna ska vara överst. Använd tabellen OrderDetails.
select 
	name as 'Blomma',
	sum(Amount) as 'Antal'
from OrderDetails
where IsDeliveryItem = 0
group by name
order by 2 desc

-- Det kanske inte är lönsamt att ha alla typer av blommor på lager. Visa de buketter som sålts 3 gånger eller färre.
select 
	name as 'Blomma',
	sum(Amount) as 'Antal'
from OrderDetails
where IsDeliveryItem = 0
group by name
having sum(Amount) <= 3
order by 2 desc

-- Visa intäkt per artikel (oavsett om det är en bukett eller frakt) med den mest inkomstbringande artikeln överst. Visa tre kolumner: artikelns namn, intäkt och antal sålda artiklar.

select
	name as 'Name',
	sum(Amount * Price) as 'Intäkt',
	sum(Amount) as 'Antal'
from OrderDetails
where IsDeliveryItem = 0
group by name
order by Intäkt desc, Name