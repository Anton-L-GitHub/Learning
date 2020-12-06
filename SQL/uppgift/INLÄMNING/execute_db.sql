use Nackademin

--- Alla tables i databasen

select *
from education

select *
from [location]

select *
from studyType

select *
from studyPoints

select *
from studyField	
	
select *
from education_webContent


--- Procedures

EXEC educations

EXEC education_search @education = 'DevOps Engineer', @location = 'Solna'

