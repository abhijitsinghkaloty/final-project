-- EXECUTED
-- users
CREATE TABLE IF NOT EXISTS users (

	id INTEGER NOT NULL,

	username TEXT NOT NULL,

	hash TEXT NOT NULL,

	PRIMARY KEY(id)

);

-- user profile
CREATE TABLE IF NOT EXISTS profile (

	person_id INTEGER NOT NULL,

	first_name TEXT,
	
	last_name TEXT,

	age INTEGER,

	country TEXT,
	-- change to online when user logs in then change back to offline when user logs out
	state TEXT DEFAULT 'offline',

	FOREIGN KEY (person_id) REFERENCES users(id)

);

-- FRIENDS
-- store user_id of user and user_id's if friends
CREATE TABLE IF NOT EXISTS friends (

	user_id INTEGER NOT NULL,

	friend INTEGER NOT NULL,

	FOREIGN KEY (user_id) REFERENCES users(id)

);

-- posts
CREATE TABLE IF NOT EXISTS posts (

	id INTEGER NOT NULL,

	user_id INTEGER NOT NULL,

	support INTEGER DEFAULT 0,

	posted TEXT NOT NULL, 

	PRIMARY KEY (id)

	FOREIGN KEY (user_id) REFERENCES users(id)
);

-- comments to posts
CREATE TABLE IF NOT EXISTS comments (

	id INTEGER NOT NULL,
	
	post_id INTEGER NOT NULL,

	comment TEXT NOT NULL,

	reply TEXT NOT NULL,

	PRIMARY KEY (id)

	FOREIGN KEY (post_id) REFERENCES posts(id)

);

-- replies to comments
CREATE TABLE IF NOT EXISTS replies (

	id INTEGER NOT NULL,

	comment_id INTEGER NOT NULL,

	reply TEXT NOT NULL,

	PRIMARY KEY (id),

	FOREIGN KEY (comment_id) REFERENCES comments(id)

);

-- feedbacks to a reply
CREATE TABLE IF NOT EXISTS feedbacks (

	reply_id INTEGER NOT NULL,

	feedback TEXT NOT NULL, 

	FOREIGN KEY (reply_id) REFERENCES replies(id)

);