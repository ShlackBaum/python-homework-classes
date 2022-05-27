CREATE TABLE IF NOT EXISTS artists (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	year INTEGER CHECK (year>=0) NOT NULL,
	artists_id INTEGER REFERENCES artists(id)
);

CREATE TABLE IF NOT EXISTS tracks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	duration INTEGER CHECK (duration>0) NOT NULL,
	album_id INTEGER REFERENCES albums(id)
);

CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	artists_id INTEGER REFERENCES artists(id)
);



