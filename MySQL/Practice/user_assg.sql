use users_schema;
/* Insert 3 users*/
insert into users_schema.users(first_name,last_name,email) values("Max","Planck","MaxPlanck@gmail.com"),("Albert","Einstein","AlbertEinstein@gmail.com"),("Tommy","Gross","TommyGross@gmail.com");
/* Retrieve data*/
select * from users_schema.users;
/*query eamil / id*/
select * from users_schema.users where email="MaxPlanck@gmail.com";
/*Last user */
select * from users_schema.users where id=3;
/*Update* UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;*/
update users_schema.users set last_name="Pancakes" where id=3;

/*Delete user 2*/
delete from users_schema.users where id=2;
/*Slect by first name*/
select * from users_schema.users order by first_name;

/*Slect by first name*/
select * from users_schema.users order by first_name desc;

