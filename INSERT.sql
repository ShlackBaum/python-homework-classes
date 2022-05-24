INSERT INTO artist(name)
	values('Britney Spears');

INSERT INTO artist(name)
	values('Elton John');
	
INSERT INTO artist(name)
	values('Vladimir Vysotskiy');
	
INSERT INTO artist(name)
	values('LilJohn');
	
INSERT INTO artist(name)
	values('Andrew Garfield');
	
INSERT INTO artist(name)
	values('Rogozin Dmitriy');
	
INSERT INTO artist(name)
	values('Britney Spears');

INSERT INTO artist(name)
	values('Courtney Cox');

INSERT INTO genre(name)
	values('Canrty');

INSERT INTO genre(name)
	values('Sad');

INSERT INTO genre(name)
	values('Joyful');

INSERT INTO genre(name)
	values('Rock');

INSERT INTO genre(name)
	values('Metal');

INSERT INTO genre(name)
	values('Pop');

INSERT INTO album(name, year)
	values('My Trouble', 2018);

INSERT INTO album(name, year)
	values('Not My Trouble', 2019);

INSERT INTO album(name, year)
	values('Sunshine', 2018);

INSERT INTO album(name, year)
	values('Friendship', 2010);

INSERT INTO album(name, year)
	values('Waves of love', 2021);

INSERT INTO album(name, year)
	values('Horrible Truth', 2009);

INSERT INTO album(name, year)
	values('Aftremath', 2022);

INSERT INTO album(name, year)
	values('Into the Deep', 2008);

INSERT INTO track(name, duration, album_id)
	values('Sex', 180, 1);

INSERT INTO track(name, duration, album_id)
	values('Love', 190, 2);
	
INSERT INTO track(name, duration, album_id)
	values('Truth', 200, 3);
	
INSERT INTO track(name, duration, album_id)
	values('Space', 185, 4);
	
INSERT INTO track(name, duration, album_id)
	values('Cosmopolitan', 197, 5);
	
INSERT INTO track(name, duration, album_id)
	values('Table and Chair', 220, 6);
	
INSERT INTO track(name, duration, album_id)
	values('Honest Pillow', 153, 7);
	
INSERT INTO track(name, duration, album_id)
	values('Johnny Revenge Doll', 197, 8);
	
INSERT INTO track(name, duration, album_id)
	values('Amber Turd', 205, 1);
	
INSERT INTO track(name, duration, album_id)
	values('Tracking Vows', 301, 2);
	
INSERT INTO track(name, duration, album_id)
	values('WowAffection', 176, 3);
	
INSERT INTO track(name, duration, album_id)
	values('Absolution', 198, 4);
	
INSERT INTO track(name, duration, album_id)
	values('My heavens', 202, 5);
	
INSERT INTO track(name, duration, album_id)
	values('Your cup', 249, 6);
	
INSERT INTO track(name, duration, album_id)
	values('Blood in my Bathroom', 226, 7);
	
INSERT INTO track(name, duration, album_id)
	values('Bottle of Fear', 380, 8);

INSERT INTO compilation (name, year)
	values('Of Love', 2018);
	
INSERT INTO compilation (name, year)
	values('Of Fear', 2019);
	
INSERT INTO compilation (name, year)
	values('Best of stuff', 2020);
	
INSERT INTO compilation (name, year)
	values('Horrible Everything', 2021);
	
INSERT INTO compilation (name, year)
	values('Togetehrness', 2022);
	
INSERT INTO compilation (name, year)
	values('Fear and Laughther', 2018);
	
INSERT INTO compilation (name, year)
	values('Pray', 2019);
	
INSERT INTO compilation (name, year)
	values('Simplicity', 2020);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(1,1);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(2,2);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(3,3);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(4,4);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(5,5);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(6,6);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(7,1);
	
INSERT INTO ArtistGenre (artist_Id, genre_Id)
	values(8,2);

	
INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(1,1);
	
INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(2,2);
	
INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(3,3);
	
INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(4,4);
	
INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(5,5);
	
INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(6,6);
	
INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(7,7);

INSERT INTO AlbumArtist (artist_Id, album_Id)
	values(8,1);

INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(1,1);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(2,2);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(3,3);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(4,4);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(5,5);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(6,6);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(7,7);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(8,8);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(9,1);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(10,2);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(11,3);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(12,4);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(13,5);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(14,6);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(15,7);
	
INSERT INTO TrackCompilation (track_Id, compilation_id)
	values(16,8);