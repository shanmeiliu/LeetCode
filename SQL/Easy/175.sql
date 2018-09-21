select FirstName, LastName, City, State
from Person left join Address 
ON Person.PersonId = Address.PersonId 
