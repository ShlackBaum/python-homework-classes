SELECT name, YEAR FROM album
	WHERE YEAR >= 2018
	
SELECT name, duration FROM track
	ORDER BY duration DESC
	LIMIT 1;

SELECT name FROM track
	WHERE duration >=210

SELECT name FROM compilation
	WHERE YEAR >=2018 AND YEAR <=2020

SELECT name FROM artist
	WHERE name NOT LIKE '% %'

SELECT name FROM track
	WHERE name iLIKE '%my%' OR name LIKE '%Мой%'
