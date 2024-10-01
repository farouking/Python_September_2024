/*specify used db*/
use books_schema;
/* First_query: create five users*/
insert into users (first_name,last_name) values("Jane","Amsden"),("Emily","Dixon"),("Theodore","Dostoevsky"),("William","Shapiro"),("Lao","Xiu");
/* Retreive All*/
select * from users;
/* Second_query: create five books*/
insert into books (title) values ("C sharp"),("Java"),("Python"),("PHP"),("Ruby");
/* Retreive All*/
select * from books;
/*Third Query update book title :UPDATE table_name SET column1 = value1, column2 = value2, ...WHERE condition; */
update books set title="C#" where ID=1;
/* Fourth Querychange the name of 4 th user to Bill*/
update users set first_name="Bill" where ID=4;
/*Fifth query  /*the user 1 has the two first books as favourite */  

insert into favorites (user_ID,book_ID) values (1,1),(1,2);
/* +++++++++++++++++*/
select *from favorites;

/*the user 2 has the three first books as favourite */

INSERT INTO favorites (user_ID,book_ID) VALUES (2,1),(2,2),(2,3);

/*the user 3 has the four first books as favourite */

INSERT INTO favorites (user_ID,book_ID) VALUES (3,1),(3,2),(3,3),(3,4);

/*the user 4 has All books as favourite */

INSERT INTO favorites (user_ID,book_ID) VALUES (4,1),(4,2),(4,3),(4,4),(4,5);

/*retrive the users that prefer the 3 rd book */

SELECT first_name, last_name FROM users
JOIN favorites on users.id = favorites.user_ID
JOIN books on books.id = favorites.book_ID
WHERE books.id = 3;

-- Query: Remove the first user of the 3rd book's favorites
DELETE from favorites where book_id = 3 AND user_id = 1;

/*the user 5 has as favourite book two . */

INSERT INTO favorites (user_ID,book_ID) VALUES (5,2);

/*user 03 favourite books */

SELECT title from books
JOIN favorites  on books.ID = favorites.book_ID
WHERE favorites.user_ID = 3;

/*All usersthat their favourite book is book5 */
SELECT users.first_name , users.last_name FROM users
join favorites on users.id = favorites.user_ID
join books on favorites.book_ID = books.id
WHERE books.id = 5;