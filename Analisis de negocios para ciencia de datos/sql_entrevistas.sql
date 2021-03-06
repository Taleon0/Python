-- 1: SQL para encontrar el segundo salario más alto de los empleados:
select MAX(Salary) from Employee WHERE Salary NOT IN (select MAX(Salary) from Employee ); 

-- 2: SQL para encontrar el salario máximo de cada departamento
SELECT DeptID, MAX(Salary) FROM Employee GROUP BY DeptID. 

-- 3: Escriba una consulta SQL para mostrar la fecha actual.
SELECT GetDate(); 

-- 4: Escriba una consulta SQL para comprobar si la fecha pasada a la consulta es la fecha del formato dado o no.
SELECT ISDATE(‘1/08/13’) AS “MM/DD/YY”;

-- 5: Escriba una consulta SQL para imprimir el nombre del empleado distinto cuya fecha de nacimiento es entre el 01/01/1960 al 31/12/1975.
SELECT DISTINCT EmpName FROM Employees WHERE DOB  BETWEEN ‘01/01/1960’ AND ‘31/12/1975’;

-- 6: Escriba una consulta SQL para encontrar el número de empleados según el género cuya fecha de nacimiento sea entre el 01/01/1960 y el 31/12/1975.
SELECT COUNT(*), sex from Employees WHERE DOB BETWEEN ‘01/01/1960’ AND ‘31/12/1975’ GROUP BY sex

--7: Escriba una consulta SQL para encontrar un empleado cuyo salario sea igual o superior a 10000.
SELECT EmpName FROM  Employees WHERE  Salary>=10000;

--8: Escriba una consulta SQL para encontrar el nombre del empleado cuyo nombre comience con "M"
SELECT * FROM Employees WHERE EmpName like ‘M%’;

-- 9: busque todos los registros de empleados que contengan la palabra “Joe”, independientemente de si se almacenó como JOE, Joe o joe.
SELECT * from Employees  WHERE  UPPER(EmpName) like '%JOE%';

-- 10: Escriba una consulta SQL para encontrar el año desde la fecha.
SELECT YEAR(GETDATE()) as “Year”;