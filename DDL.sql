CREATE TABLE Customer_T
(CustomerID NUMERIC(11,0) NOT NULL,
CustomerName VARCHAR(40) NOT NULL,
CustomerEmail VARCHAR(80) NOT NULL,
CustomerPassword VARCHAR(20) NOT NULL,
CustomerPhoneNumber NUMERIC(11) NOT NULL,
CONSTRAINT Customer_PK PRIMARY KEY (CustomerID));

CREATE TABLE Order_T
(OrderID NUMERIC(11,0) NOT NULL,
OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
OrderStatus VARCHAR(10) NOT NULL, 
CustomerID NUMERIC(11,0) NOT NULL,
CONSTRAINT OrderID_PK PRIMARY KEY(OrderID),
CONSTRAINT Order_FK1 FOREIGN KEY (CustomerID) REFERENCES Customer_T(CustomerID));

CREATE TABLE Category_T
(CategoryID NUMERIC(2) NOT NULL,
CategoryType VARCHAR(20) NOT NULL,
CONSTRAINT CategoryID_PK PRIMARY KEY (CategoryID));

CREATE TABLE Product_T
(ProductID  NUMERIC(11,0) NOT NULL,
ProductDescription VARCHAR(200) NOT NULL,
ProductSize VARCHAR(3) NOT NULL,
ProductPrice NUMERIC(6,2) NOT NULL,
ProductColor VARCHAR(20) NOT NULL,
ProductAvailableQuantity NUMERIC (3) NOT NULL,
ProductSKUCode VARCHAR(15) NULL,
ProductImageFileName VARCHAR(40) NULL,
CategoryID NUMERIC(2) NOT NULL,
ColorID NUMERIC(2) NOT NULL,
SizeID NUMERIC(2) NOT NULL,
CONSTRAINT ProductID_PK PRIMARY KEY (ProductID),
CONSTRAINT CategoryID_FK1 FOREIGN KEY (CategoryID)REFERENCES Category_T(CategoryID),
CONSTRAINT SizeID_FK2 FOREIGN KEY (SizeID)REFERENCES Size_T(SizeID),
CONSTRAINT ColorID_FK3 FOREIGN KEY (ColorID)REFERENCES Color_T(ColorID));


CREATE TABLE OrderLine_T
(OrderLineID NUMERIC(11,0) NOT NULL,
ProductQuantity NUMERIC(5) NOT NULL,
ProductID  NUMERIC(11,0) NOT NULL,
OrderID NUMERIC(11,0) NOT NULL,
CONSTRAINT OrderLineID_PK PRIMARY KEY(OrderLineID),
CONSTRAINT ProductID_FK1 FOREIGN KEY (ProductID)REFERENCES Product_T(ProductID),
CONSTRAINT OrderID_FK2 FOREIGN KEY(OrderId) REFERENCES Order_T(OrderID));


CREATE TABLE BillingAddress_T
(BillingAddressID NUMERIC(11,0) NOT NULL,
CustomerStreet VARCHAR(20) NOt NULL,
CustomerCity VARCHAR(20) NOT NULL,
CustomerState CHAR(2) NOT NULL,
CustomerZipCode VARCHAR(10) NOT NULL,
CustomerID NUMERIC(11,0) NOt NULL,
CONSTRAINT BillingAddressID_PK PRIMARY KEY(BillingAddressID),
CONSTRAINT CustomerID_FK1 FOREIGN KEY (CustomerID) REFERENCES Customer_T(CustomerID));

CREATE TABLE ShippingAddress_T
(ShippingAddressID NUMERIC(11,0) NOT NULL,
CustomerStreet VARCHAR(20) NOt NULL,
CustomerCity VARCHAR(20) NOT NULL,
CustomerState CHAR(2) NOT NULL,
CustomerZipCode VARCHAR(10) NOT NULL,
CustomerID NUMERIC(11,0) NOt NULL,
CONSTRAINT ShippingAddressID_PK PRIMARY KEY(ShippingAddressID),
CONSTRAINT CustomerID_FK FOREIGN KEY (CustomerID) REFERENCES Customer_T(CustomerID));

CREATE TABLE Color_T
(ColorID NUMERIC(2) NOT NULL,
Color VARCHAR(20) NOT NULL,
CONSTRAINT ColorID_PK PRIMARY KEY (ColorID));

CREATE TABLE Size_T
(SizeID NUMERIC(2) NOT NULL,
Size VARCHAR(20) NOT NULL,
CONSTRAINT SizeID_PK PRIMARY KEY (SizeID));


