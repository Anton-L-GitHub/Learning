----- 1 ------

SELECT * FROM Employee

----- 2 ------

SELECT *
FROM Employee
WHERE HireDate = '2002-12-03'

----- 3 ------

SELECT *
FROM Employee
WHERE HireDate > '2000-01-01'

----- 4 ------

SELECT 
	Lastname,
	Job,
	Salary,
	Commission
FROM Employee
WHERE
	Salary > 20000

----- 5 ------

SELECT
	Firstname,
	Lastname,
	Salary + isnull(Commission, 0) as 'New salary'
FROM Employee

----- 6 ------

SELECT 
	Lastname,
	Salary,
	Salary * 1.1 AS 'New salary'
FROM Employee
WHERE Salary < 10000

----- 7 ------

SELECT
	Lastname,
	Salary,
	Salary * 0.3 AS 'Skatt'
FROM Employee

----- 8 ------

SELECT 
	Lastname,
	Salary,
	Commission
FROM Employee
WHERE Commission IS NULL

----- 9 ------
SELECT
	Lastname,
	Job,
	Salary
FROM Employee
WHERE 
Job = 'Chef' and
Lastname = 'Jones'

----- 10 ------

SELECT
	Lastname,
	Job,
	Salary
FROM Employee
WHERE 
Job = 'Chef' and
Lastname != 'Jones'

----- 11 ------

SELECT *
FROM Employee
WHERE 
Lastname LIKE 'J%' or
Lastname LIKE '%ar%'

----- 12 ------

SELECT
	lower(firstname + '.' + lastname + '@nackademin.com') as Email
FROM Employee
