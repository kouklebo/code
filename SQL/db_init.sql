
SHOW DATABASES;
DROP DATABASE GLO_2005_projet;
CREATE DATABASE GLO_2005_projet;
use GLO_2005_projet;
SHOW TABLES;
SELECT * FROM data_beers;
SELECT * FROM order_item;
SELECT * FROM data_customers;
INSERT INTO data_beers (id,Name,Brewery,Style,Alcohol_content,Calories,Carbohydrates,Sugar,Ingredients,Country,Dispense,Comments,Price,release_date,rating)
VALUES (1, "Wet Hopped Pilsner", "Insel-Brauerei", "pilsner",0.005, "106 (per 330ml bottle)","21g (per 330ml bottle)","1.5g (per 330ml bottle)","water, barley, wheat, hops, yeast", "Germany", "bottle (330ml)","The main thing the hops contribute to is the bitterness, which grows during each sip until item s almost lip puckering. Yet item s balanced with those other, sweeter flavours.",4.99,2017,10);

CREATE TABLE  IF NOT EXISTS data_beers
(
    id              INT,
    Name            VARCHAR(100),
    Brewery         VARCHAR(100), 
    Style           VARCHAR(100),
    Alcohol_content FLOAT(1),
    Calories        VARCHAR(100),
    Carbohydrates   VARCHAR(100),
    Sugar           VARCHAR(100),
    Ingredients     varchar(300),
    Country         VARCHAR(100),
    Dispense        VARCHAR(100),
    Comments        VARCHAR(500),
    Price           FLOAT(2),
    release_date    YEAR,
    rating          TINYINT(1),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS credit_Card
(
    CC_number VARCHAR(16),
    CC_expiration_date DATETIME,
    PRIMARY KEY (CC_number)
);

CREATE TABLE IF NOT EXISTS data_customers
(
    customer_id              INT,
    last_name       VARCHAR(500),
    first_name      VARCHAR(500),
    Password        VARCHAR(500),
    birth_date      DATE,
    email           VARCHAR(500),
    phone_number    DECIMAL,
    Fidelity_point  INT,
    Billing_address VARCHAR(500),
    Credit_card VARCHAR(16),
    PRIMARY KEY(customer_id),
    FOREIGN KEY(Credit_card)
        REFERENCES credit_Card (CC_number)

);


CREATE TABLE IF NOT EXISTS supplier_order
(
    id INT,
    delivery_date DATE,
    Product_id INT,
    Cost FLOAT(2),
    Quantity INT,
    PRIMARY KEY (id),
    FOREIGN KEY (Product_id)
        REFERENCES data_beers (id)

);

CREATE TABLE IF NOT EXISTS customer_Order
(
    Order_id INT,
    Client_id INT,
    Total_price FLOAT(2),
    Order_status ENUM('Processing', 'Preparing', 'Ready to Pick Up', 'Picked Up'),
    PRIMARY KEY (Order_id),
    FOREIGN KEY (Client_id)
        REFERENCES data_customers(customer_id)
);

CREATE TABLE IF NOT EXISTS order_item
(
    item_id INT,
    Order_id INT,
    Beer_id INT,
    Quantity INT,
    PRIMARY KEY (item_id),
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
    Customer_id INT,
    rating TINYINT,
    PRIMARY KEY (Beer_id, Customer_id),
    FOREIGN KEY (Beer_id)
        REFERENCES data_beers(id),
    FOREIGN KEY (Customer_id)
        REFERENCES data_customers(customer_id)
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

