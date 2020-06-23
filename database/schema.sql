-- EXECUTED
CREATE TABLE IF NOT EXISTS users (

	id INTEGER NOT NULL,

	username TEXT NOT NULL,

	hash TEXT NOT NULL,

	PRIMARY KEY(id)

);

-- EXECUTED
CREATE TABLE IF NOT EXISTS profile (

	person_id INTEGER NOT NULL,

	first_name TEXT,
	
	last_name TEXT,

	age INTEGER,

	country TEXT,

	FOREIGN KEY (person_id) REFERENCES users(id)

);

CREATE TABLE IF NOT EXISTS posts (

	user_id INTEGER NOT NULL,

	support INTEGER DEFAULT 0,

	posted TEXT NOT NULL, 

	FOREIGN KEY (user_id) REFERENCES users(id)
);