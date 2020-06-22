CREATE TABLE IF NOT EXISTS users (

	id INTEGER AUTOINCREMENT NOT NULL,

	username TEXT,

	hash TEXT NOT NULL,

	PRIMARY KEY(id)

);

CREATE TABLE IF NOT EXISTS person (

	person_id INTEGER NOT NULL,

	first_name TEXT,
	
	last_name TEXT,

	age INTEGER,

	FOREIGN KEY (person_id) REFERENCES users(id)

);

