select a.name as Employee
From Employee a
Join Employee b on a.managerId=b.id
where a.salary>b.salary;