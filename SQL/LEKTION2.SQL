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
SELECT *
FROM Department
FULL JOIN Employee
ON Department.DeptID = Employee.EmpID
WHERE
DDeptID IS NOT NULL