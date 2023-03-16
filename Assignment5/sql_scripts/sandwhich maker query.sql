CREATE SCHEMA sandwhich_makers;

CREATE TABLE sandwhiches (
sandwhich_size varchar(50),
price decimal(5,2)
);
INSERT INTO sandwhiches(sandwhich_size, price) VALUES
('small',1.75),
('medium',3.25),
('large',5.5);
SELECT * FROM sandwhiches;

CREATE TABLE resources (
food varchar(50),
amount varchar(50)

);
INSERT INTO resources(food, amount) VALUES
('bread',12),
('ham',18),
('cheese',24);
SELECT * FROM resources;
CREATE TABLE sandwich_ingredients (
  sandwich_size varchar(50),
  item varchar(50),
  amount_needed int
);

INSERT INTO sandwich_ingredients (sandwich_size, item, amount_needed) VALUES
('small', 'bread', 2),
('small', 'ham', 2),
('small', 'cheese', 1),
('medium', 'bread', 3),
('medium', 'ham', 3),
('medium', 'cheese', 2),
('large', 'bread', 4),
('large', 'ham', 4),
('large', 'cheese', 3);
SELECT * FROM sandwich_ingredients;