use mydb;
select * from names;
/* INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');

*/
insert into names (name) value ("Farouk SOUISSI");
/* BONUS 1; insert more than name in one statment*/
insert into names (name) value ("Jhon DOE"),("Ali BOOD"),("Amir KARIMI");
/*BONUS 2* UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;*/

UPDATE names
SET name = ("Farouq SOUISSI")
WHERE ID=1;
/*DELETE FROM table_name WHERE condition;*/
DELETE FROM names WHERE ID=2;
