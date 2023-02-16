-- Create a table with a unique id and default value
CREATE TABLE IF NOT EXISTS unique_id (
	id INTEGER DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
