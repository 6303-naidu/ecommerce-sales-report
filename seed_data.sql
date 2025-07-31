-- Insert sample customers
INSERT INTO customers VALUES (1, 'Alice', 'alice@email.com');
INSERT INTO customers VALUES (2, 'Bob', 'bob@email.com');

-- Insert sample products
INSERT INTO products VALUES (1, 'Laptop', 'Electronics', 800.00);
INSERT INTO products VALUES (2, 'Headphones', 'Electronics', 150.00);

-- Insert sample orders
INSERT INTO orders VALUES (1, 1, '2024-07-01');
INSERT INTO orders VALUES (2, 2, '2024-07-05');

-- Insert order items
INSERT INTO order_items VALUES (1, 1, 1, 1); -- Alice buys 1 Laptop
INSERT INTO order_items VALUES (2, 2, 2, 2); -- Bob buys 2 Headphones