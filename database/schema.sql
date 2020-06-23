CREATE TABLE IF NOT EXISTS users (

	id INTEGER NOT NULL,

	username TEXT NOT NULL,

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

