CREATE DATABASE users;
CREATE USER trippi WITH ENCRYPTED PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE users TO trippi;
\c users trippi;
GRANT ALL ON SCHEMA public TO trippi;

