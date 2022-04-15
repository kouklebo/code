#fonction utile pour voir son mot de passe
CREATE DATABASE GLO_2005_projet;
use GLO_2005_projet;
SELECT * FROM data_customers;

#un utilisateur par defaut
INSERT INTO pwd (pseudo, motdepasse) VALUES ('Jennifer1','mdp1');

#creer notre base de donnees rapidement selectionner tout et runner
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


CREATE TABLE IF NOT EXISTS data_customers
(
    pseudo          VARCHAR(50) NOT NULL ,
    last_name       VARCHAR(50),
    first_name      VARCHAR(100),
    birth_date      DATE,
    email           VARCHAR(500) NOT NULL,
    phone_number    DECIMAL,
    Billing_address VARCHAR(500),
    Credit_card VARCHAR(16),
    PRIMARY KEY(Pseudo),
    CONSTRAINT Credit_card UNIQUE(Credit_card)
);


CREATE TABLE IF NOT EXISTS credit_Card
(
    CC_number VARCHAR(16),
    CC_expiration_date DATETIME,
    PRIMARY KEY (CC_number),
    FOREIGN KEY(CC_number)
        REFERENCES data_customers (Credit_card)
        ON UPDATE CASCADE
        ON DELETE CASCADE


);


CREATE TABLE IF NOT EXISTS pwd
(
    pseudo VARCHAR(50),
    motdepasse VARCHAR(100),
    PRIMARY KEY (pseudo)
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
        ON UPDATE CASCADE
        ON DELETE CASCADE

);


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
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS order_item
(
    Client_id VARCHAR(50),
    Order_id INT,
    Beer_id INT,
    Quantity INT,
    Total_price FLOAT(3),
    PRIMARY KEY (Client_id, Order_id),
    FOREIGN KEY (Client_id)
        REFERENCES data_customers(pseudo),
    FOREIGN KEY (Beer_id)
        REFERENCES data_beers (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (Order_id)
        REFERENCES customer_Order(Order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE

);


CREATE TABLE IF NOT EXISTS stock
(
    Beer_id INT,
    Quantity INT,
    FOREIGN KEY (Beer_id)
        REFERENCES data_beers(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
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


CREATE TRIGGER updateQuantityAfterUpdate AFTER INSERT ON customer_Order
    FOR EACH ROW UPDATE stock
    SET stock.Quantity = stock.Quantity - (SELECT Quantity FROM customer_Order C WHERE C.Beer_id = NEW.Beer_id);


CREATE TRIGGER updateQuantityAfterUpdate2 AFTER INSERT ON supplier_order
    FOR EACH ROW UPDATE stock
    SET stock.Quantity = stock.Quantity - (SELECT Quantity FROM supplier_order S WHERE S.Product_id = NEW.Product_id);


DELIMITER //
CREATE TRIGGER Creation_pwd
   AFTER INSERT ON data_customers
    FOR EACH ROW
    BEGIN
      INSERT INTO pwd(pseudo, motdepasse) VALUES (NEW.pseudo,CONCAT(NEW.pseudo,ROUND( RAND() * 100 )));
    end//
DELIMITER ;


