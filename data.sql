INSERT INTO category_t
VALUE 
(1,"Skirt"),
(2,"Shirt"),
(3,"Dress"),
(4,"Pants"),
(5,"Sweater");



INSERT INTO Product_t
VALUES 
(01, "High-waisted mini skirt with elastic waistband.","S",50.25,"Blue", 15,123456,"Image01",1),
(02, "Mid-rise pants with side pockets and back false welt pockets. 
Front zip, metal hook, and interior button closure.","M",45.90,"Blue", 15,159753,"Image02",4),
(05, "Petite recycled lace trim long sleeve mini dress","L",20.20,"Blue", 15,165412,"Image03",3),
(06, "Strap detail slip dress","S",74.00,"Gold", 15,147258,"Image04",3),
(10, "Full cut round neck sleeveless top","M",85.89,"Black", 15,258369,"Image05",2);
(03, "High-waisted mini skirt with elastic waistband.","M",50.25,"Red", 5,1234567,"Image01",1),
(04, "High-waisted mini skirt with elastic waistband.","L",50.25,"Blue", 10,1234568,"Image01",1),
(07, "Strap detail slip dress","M",74.00,"Gold", 10,1472581,"Image04",3),
(08, "Strap detail slip dress","L",74.00,"Gold", 13,1472582,"Image04",3),
(09, "Strap detail slip dress","XL",74.00,"Gold", 11,1472583,"Image04",3),
(11, "Full cut round neck sleeveless top","S",85.89,"Black", 10,2583691,"Image05",2);
(12, "Full cut round neck sleeveless top","L",85.89,"Black", 18,2583692,"Image05",2);
(13, "Cable knitted long sleeved sweater","M",125.25,"Black", 10,552413,"Image06",5);

INSERT INTO `billingaddress_t` (`BillingAddressID`, `CustomerStreet`, `CustomerCity`, `CustomerState`, `CustomerZipCode`, `CustomerID`) VALUES
('1', '100 Forest Road', 'Oz', 'KS', '71234', '3330'),
('2', '144 Yale Avenue', 'Chicago', 'IL', '66666', '1111'),
('3', '123 Harvard Avenue', 'Chicago', 'IL', '66770', '2220'),
('5', '333 Yellow Rd', 'Oz', 'KS', '71234', '3330');


INSERT INTO `customer_t` (`CustomerID`, `CustomerName`, `CustomerEmail`, `CustomerPassword`, `CustomerPhoneNumber`) VALUES
('1111', 'Alex Jones', 'aj@customer.com', 'password1111', '1'),
('2220', 'Jane Smith', 'jsmith22@customer.com', 'password2220', '99'),
('3330', 'Ali Fang', 'afang@companyx.com', 'password1', '889');


INSERT INTO `orderline_t` (`OrderLineID`, `ProductQuantity`, `ProductID`, `OrderID`) VALUES
('1000', '2', '5', '101'),
('1001', '1', '3', '102'),
('1003', '1', '4', '104'),
('1004', '1', '5', '103'),
('1005', '1', '2', '102'),
('1006', '1', '3', '104');


INSERT INTO `order_t` (`OrderID`, `OrderDate`, `OrderStatus`, `CustomerID`) VALUES
('101', '2021-12-03 18:33:19', 'Completed', '3330'),
('102', '2021-12-03 18:33:19', 'Processing', '2220'),
('103', '2021-12-03 18:34:15', 'Shipped', '2220'),
('104', '2021-12-03 18:34:15', 'Processing', '1111');


INSERT INTO `product_t` (`ProductID`, `ProductDescription`, `ProductSize`, `ProductPrice`, `ProductColor`, `ProductAvailableQuantity`, `ProductSKUCode`, `ProductImageFileName`, `CategoryID`) VALUES
('1', 'High-waisted mini skirt with elastic waistband.', 'S', '50.25', 'Blue', '15', '123456', 'Image01', '1'),
('2', 'Mid-rise pants with side pockets and back false welt pockets. \r\nFront zip, metal hook, and interior button closure.', 'M', '45.90', 'Blue', '15', '159753', 'Image02', '4'),
('3', 'Petite recycled lace trim long sleeve mini dress', 'L', '20.20', 'Blue', '15', '165412', 'Image03', '3'),
('4', 'Strap detail slip dress', 'S', '74.00', 'Gold', '15', '147258', 'Image04', '3'),
('5', 'Full cut round neck sleeveless top', 'M', '85.89', 'Black', '15', '258369', 'Image05', '2');



INSERT INTO `shippingaddress_t` (`ShippingAddressID`, `CustomerStreet`, `CustomerCity`, `CustomerState`, `CustomerZipCode`, `CustomerID`) VALUES
('110', '123 Yale Avenue', 'Chicago', 'Il', '60066', '2220'),
('111', '144 Yale Avenue', 'Chicago', 'Il', '66666', '2220'),
('112', '123 Princeton Avenue', 'Chicago', 'Il', '60059', '1111'),
('113', '100 Forest Road', 'Oz', 'KS', '71234', '3330'),
('114', '110 Yale Avenue', 'Chicago', 'Il', '60066', '1111'),
('115', '220 Hale Avenue', 'Chicago', 'Il', '60066', '1111'),
('116', '333 Yellow Rd', 'Oz', 'KS', '72345', '3330');

