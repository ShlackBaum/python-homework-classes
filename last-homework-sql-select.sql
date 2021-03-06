SELECT genre.name, count(genre.name) FROM artist
LEFT JOIN artistgenre ON artist.id = artistgenre.artist_id
LEFT JOIN genre ON artistgenre.genre_id = genre.id
GROUP BY genre.name
ORDER BY count(genre.name) DESC;

SELECT count(track.name) FROM track
LEFT JOIN album ON track.album_id = album.id
WHERE album.year >=2019 AND album.YEAR <=2020

SELECT avg(track.duration), album.name FROM track
LEFT JOIN album ON track.album_id = album.id
GROUP BY album.name;

SELECT artist.name FROM artist
LEFT JOIN albumartist ON artist.id = albumartist.album_id
LEFT JOIN album ON albumartist.album_id = album.id
WHERE NOT YEAR = 2020;

SELECT DISTINCT compilation.name FROM compilation
LEFT JOIN trackcompilation ON compilation.id = trackcompilation.compilation_id 
LEFT JOIN track ON trackcompilation.compilation_id = track.id
LEFT JOIN album ON track.album_id = album.id
LEFT JOIN albumartist ON album.id = albumartist.album_id
LEFT JOIN artist ON albumartist.artist_id = artist.id 
WHERE artist.name = 'LilJohn';

SELECT album.name album FROM album
INNER JOIN albumartist ON album.id = albumartist.album_id
INNER JOIN artist ON albumartist.artist_id = artist.id 
INNER JOIN artistgenre ON albumartist.artist_id = artist.id 
INNER JOIN genre ON artistgenre.genre_id = genre.id
WHERE artist.id = artistgenre.artist_ID
GROUP BY album
HAVING count(artist.id) > 1;

SELECT track.name track FROM track 
FULL OUTER JOIN trackcompilation ON trackcompilation.track_id = track.id
WHERE trackcompilation.track_id IS null;

SELECT artist.name FROM artist
LEFT JOIN albumartist ON artist.id = albumartist.artist_id
LEFT JOIN album ON album.id = albumartist.album_id 
LEFT JOIN track ON album.id = track.album_id
WHERE track.duration = 
(SELECT min(track.duration) FROM artist
LEFT JOIN albumartist ON artist.id = albumartist.artist_id
LEFT JOIN album ON album.id = albumartist.album_id 
LEFT JOIN track ON album.id = track.album_id);

SELECT album.name album, count(track.name) FROM album
LEFT JOIN track ON album.id = track.album_id
GROUP BY album.name
HAVING count(track.name) = (
SELECT count(track.name) track FROM album
LEFT JOIN track ON album.id = track.album_id
GROUP BY album.name
ORDER BY count(track.name)
LIMIT 1
);
