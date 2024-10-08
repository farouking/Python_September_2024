/*Queries_World_BD*/
use world;
SELECT * FROM countries;
SELECT * FROM cities;
SELECT * FROM languages;
/* First Query*/
SELECT countries.name as name, languages.language as language, languages.percentage as percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;
/* Second Query*/
SELECT countries.name as name, count(DISTINCT  world.cities.name)  as number_of_cities 
FROM world.cities JOIN world.cities ON world.cities.contry_id = world.countries.id
ORDER BY number_of_cities DESC;

SELECT countries.name as name, COUNT(cities.name) as number_of_cities
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY number_of_cities DESC;

/* Third Query*/
SELECT   cities.name as Name , cities.population as Population FROM cities 
JOIN countries ON countries.id = cities.country_id
where countries.name = 'mexico' and cities.population > 500000
ORDER BY cities.population DESC ;

/*Fourth Query*/
SELECT languages.language , percentage FROM languages 
join countries on languages.country_id=countries.id
where percentage > 89
ORDER BY percentage DESC ;

/*Fifth Query*/

SELECT name,population,surface_area FROM countries where surface_area < 501 and population > 100000;

/*Sixth Query*/

SELECT name,government_form,life_expectancy , capital FROM countries where government_form='constitutional Monarchy'
 and capital > 200 and life_expectancy > 75;

/*Sixth Query*/

SELECT countries.name AS Country_Name,cities.name AS City_Name,cities.district As District,cities.population As Population FROM cities 
join countries on countries.id =country_id 
WHERE countries.name = 'Argentina';

/*Eightith Query*/
SELECT countries.region , COUNT(countries.name) AS Number_of_Countries FROM countries 
group by countries.region
order by Number_of_Countries DESC;
