-- script creates a second table in the database hbtn-0c_0
-- after creating the table data is then populated to the table
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score)
VALUES('1', 'John', 10),
('2', 'Alex', '3'),
('3', 'Bob', '14'),
('4', 'George', '8');
