CREATE DATABASE IF NOT EXISTS shopping_cart;
USE shopping_cart;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO products (name, price) VALUES
('Laptop', 60000),
('Mouse', 500),
('Keyboard', 1500),
('Headphones', 2000);
