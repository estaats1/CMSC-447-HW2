DROP TABLE IF EXISTS users;

CREATE TABLE users (name TEXT NOT NULL, id INTEGER NOT NULL PRIMARY KEY, points INTEGER NOT NULL);

INSERT INTO users (name, id, points) VALUES ('Steve Smith', 211, 80);
INSERT INTO users (name, id, points) VALUES ('Jian Wong', 122, 92);
INSERT INTO users (name, id, points) VALUES ('Chris Peterson', 213, 91);
INSERT INTO users (name, id, points) VALUES ('Sai Patel', 524, 94);
INSERT INTO users (name, id, points) VALUES ('Andrew Whitehead', 425, 99);
INSERT INTO users (name, id, points) VALUES ('Lynn Roberts', 626, 90);
INSERT INTO users (name, id, points) VALUES ('Robert Sanders', 287, 75);