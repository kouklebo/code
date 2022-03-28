
SHOW DATABASES;
DROP DATABASE GLO_2005_projet;
CREATE DATABASE GLO_2005_projet;
use GLO_2005_projet;
SHOW TABLES;
SELECT * FROM data_beers;
SELECT * FROM order_item;
SELECT * FROM data_customers;
SELECT * FROM pwd;
INSERT INTO data_beers (id, Name, Brewery, Style, Alcohol_content, Price, rating)
VALUES (1,'Wet Hopped Pilsner','Insel-Brauerei','Other',0.05,4.99,10);

INSERT INTO data_beers (id, Name, Brewery, Style, Alcohol_content, Price, rating)
VALUES (2,'Lemongrass Lager','Toast and Teapigs','lager',0.005,9.99,7);

CREATE TABLE  IF NOT EXISTS data_beers
(
    id              INT AUTO_INCREMENT,
    Name            VARCHAR(100),
    Brewery         VARCHAR(100), 
    Style           VARCHAR(100),
    Alcohol_content FLOAT(1),
    Price           FLOAT(2),
    rating          INT,
    PRIMARY KEY(id)
);
SELECT * FROM credit_Card;
INSERT INTO credit_Card (CC_number, CC_expiration_date) VALUES ('1234567890',20221219);
CREATE TABLE IF NOT EXISTS credit_Card
(
    CC_number VARCHAR(16),
    CC_expiration_date DATETIME,
    PRIMARY KEY (CC_number)
);
SELECT * FROM data_customers;

CREATE TABLE IF NOT EXISTS data_customers
(
    pseudo          VARCHAR(50),
    last_name       VARCHAR(500),
    first_name      VARCHAR(500),
    birth_date      DATE,
    email           VARCHAR(500),
    phone_number    DECIMAL,
    Billing_address VARCHAR(500),
    Credit_card VARCHAR(16),
    PRIMARY KEY(Pseudo),
    FOREIGN KEY(Credit_card)
        REFERENCES credit_Card (CC_number)
);

CREATE TABLE IF NOT EXISTS supplier_order
(
    id INT AUTO_INCREMENT,
    delivery_date DATE,
    Product_id INT,
    Cost FLOAT(2),
    Quantity INT,
    PRIMARY KEY (id),
    FOREIGN KEY (Product_id)
        REFERENCES data_beers (id)
);

ALTER TABLE customer_Order CHANGE Client_id Client_id VARCHAR(50);
CREATE TABLE IF NOT EXISTS customer_Order
(
    Order_id INT AUTO_INCREMENT,
    Client_id VARCHAR(50),
    Beer_id INT,
    Quantity INT,
    Total_price FLOAT(2),
    PRIMARY KEY (Order_id),
    FOREIGN KEY (Client_id)
        REFERENCES data_customers(pseudo),
    FOREIGN KEY (Beer_id)
        REFERENCES data_beers(id)
);

CREATE TABLE IF NOT EXISTS order_item
(
    Client_id VARCHAR(50),
    Order_id INT,
    Beer_id INT,
    Quantity INT,
    Total_price FLOAT(2),
    PRIMARY KEY (Client_id, Order_id),
    FOREIGN KEY (Client_id)
        REFERENCES data_customers(pseudo),
    FOREIGN KEY (Beer_id)
        REFERENCES data_beers (id),
    FOREIGN KEY (Order_id)
        REFERENCES customer_Order(Order_id)
);

CREATE TABLE IF NOT EXISTS stock
(
    Beer_id INT,
    Quantity INT,
    FOREIGN KEY (Beer_id)
        REFERENCES data_beers(id)
);

CREATE TABLE IF NOT EXISTS rating
(
    Beer_id INT,
    Customer_id VARCHAR(50),
    rating TINYINT,
    PRIMARY KEY (Beer_id, Customer_id),
    FOREIGN KEY (Beer_id)
        REFERENCES data_beers(id),
    FOREIGN KEY (Customer_id)
        REFERENCES data_customers(pseudo)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TRIGGER updateBeerAvgRating AFTER INSERT ON rating
    FOR EACH ROW UPDATE data_beers
    SET rating = (SELECT AVG(rating) FROM rating R WHERE R.Beer_id = NEW.Beer_id)
    WHERE id = NEW.Beer_id;

CREATE TRIGGER updateBeerAvgRatingAfterUpdate AFTER UPDATE ON rating
    FOR EACH ROW UPDATE data_beers
    SET rating = (select AVG(rating) FROM rating R WHERE R.Beer_id = NEW.Beer_id)
    WHERE id = NEW.Beer_id;

CREATE TRIGGER updateQuantityAfterUpdate AFTER INSERT ON order_item
    FOR EACH ROW UPDATE stock
    SET stock.Quantity = stock.Quantity - (SELECT Quantity FROM order_item O WHERE O.item_id = NEW.item_id);

CREATE TRIGGER updateQuantityAfterUpdate2 AFTER INSERT ON supplier_order
    FOR EACH ROW UPDATE stock
    SET stock.Quantity = stock.Quantity - (SELECT Quantity FROM supplier_order S WHERE S.Product_id = NEW.Product_id);

SELECT * FROM data_customers;
SELECT * FROM credit_Card;

