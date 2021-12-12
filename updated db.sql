
CREATE TABLE `billingaddress_t` (
  `BillingAddressID` decimal(11,0) NOT NULL,
  `CustomerStreet` varchar(20) NOT NULL,
  `CustomerCity` varchar(20) NOT NULL,
  `CustomerState` char(2) NOT NULL,
  `CustomerZipCode` varchar(10) NOT NULL,
  `CustomerID` decimal(11,0) NOT NULL);


INSERT INTO `billingaddress_t` (`BillingAddressID`, `CustomerStreet`, `CustomerCity`, `CustomerState`, `CustomerZipCode`, `CustomerID`) VALUES
('1', '100 Forest Road', 'Oz', 'KS', '71234', '3330'),
('2', '144 Yale Avenue', 'Chicago', 'IL', '66666', '1111'),
('3', '123 Harvard Avenue', 'Chicago', 'IL', '66770', '2220'),
('5', '333 Yellow Rd', 'Oz', 'KS', '71234', '3330');


CREATE TABLE `category_t` (
  `CategoryID` decimal(2,0) NOT NULL,
  `CategoryType` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `category_t` (`CategoryID`, `CategoryType`) VALUES
('1', 'Skirt'),
('2', 'Shirt'),
('3', 'Dress'),
('4', 'Pants'),
('5', 'Sweater');


CREATE TABLE `color_t` (
  `ColorID` decimal(2,0) NOT NULL,
  `Color` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `color_t` (`ColorID`, `Color`) VALUES
('1', 'Red'),
('2', 'Blue'),
('3', 'Green'),
('4', 'Yellow'),
('5', 'White'),
('6', 'Black'),
('7', 'Orange'),
('8', 'Purple');


CREATE TABLE `customer_t` (
  `CustomerID` decimal(11,0) NOT NULL,
  `CustomerName` varchar(40) NOT NULL,
  `id` decimal(11,0) NOT NULL,
  `CustomerPhoneNumber` decimal(11,0) NOT NULL);


INSERT INTO `customer_t` (`CustomerID`, `CustomerName', `id`, `CustomerPhoneNumber`) VALUES
('1111', 'Alex Jones', 'aj@customer.com', '1',  '122'),
('2220', 'Jane Smith', 'jsmith22@customer.com', '2', '99'),
('3330', 'Ali Fang', 'afang@companyx.com', '10', '889');


CREATE TABLE `orderline_t` (
  `OrderLineID` decimal(11,0) NOT NULL,
  `ProductQuantity` decimal(5,0) NOT NULL,
  `ProductID` decimal(11,0) NOT NULL,
  `OrderID` decimal(11,0) NOT NULL
);


INSERT INTO `orderline_t` (`OrderLineID`, `ProductQuantity`, `ProductID`, `OrderID`) VALUES
('1000', '2', '5', '101'),
('1001', '1', '3', '102'),
('1003', '1', '4', '104'),
('1004', '1', '5', '103'),
('1005', '1', '2', '102'),
('1006', '1', '3', '104');


CREATE TABLE `order_t` (
  `OrderID` decimal(11,0) NOT NULL,
  `OrderDate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `OrderStatus` varchar(10) NOT NULL,
  `CustomerID` decimal(11,0) NOT NULL
);


INSERT INTO `order_t` (`OrderID`, `OrderDate`, `OrderStatus`, `CustomerID`) VALUES
('101', '2021-12-04 00:33:19', 'Completed', '3330'),
('102', '2021-12-04 00:33:19', 'Processing', '2220'),
('103', '2021-12-04 00:34:15', 'Shipped', '2220'),
('104', '2021-12-04 00:34:15', 'Processing', '1111');


CREATE TABLE `product_t` (
  `ProductID` decimal(11,0) NOT NULL,
  `ProductDescription` varchar(200) NOT NULL,
  `ProductSize` varchar(3) NOT NULL,
  `ProductPrice` decimal(6,2) NOT NULL,
  `ProductColor` varchar(20) NOT NULL,
  `ProductAvailableQuantity` decimal(3,0) NOT NULL,
  `ProductSKUCode` varchar(15) NOT NULL,
  `ProductImageFileName` varchar(40) NOT NULL,
  `CategoryID` decimal(2,0) NOT NULL,
  `ColorID` decimal(2,0) NOT NULL,
  `SizeID` decimal(2,0) NOT NULL
);


INSERT INTO `product_t` (`ProductID`, `ProductDescription`, `ProductSize`, `ProductPrice`, `ProductColor`, `ProductAvailableQuantity`, `ProductSKUCode`, `ProductImageFileName`, `CategoryID`, `ColorID`, `SizeID`) VALUES
('1', 'High-waisted mini skirt with elastic waistband.', 'S', '50.25', 'Blue', '15', '123456', 'Image01', '1', '2', '2'),
('2', 'Mid-rise pants with side pockets and back false welt pockets. Front zip, metal hook, and interior button closure.', 'M', '45.90', 'Blue', '15', '159753', 'Image02', '4', '2', '3'),
('3', 'Petite recycled lace trim long sleeve mini dress', 'L', '20.20', 'Blue', '15', '165412', 'Image03', '3', '2', '4'),
('4', 'Strap detail slip dress', 'S', '74.00', 'Yellow', '15', '147258', 'Image04', '3', '4', '2'),
('5', 'Full cut round neck sleeveless top', 'M', '85.89', 'Black', '15', '258369', 'Image05', '2', '6', '3');


CREATE TABLE `shippingaddress_t` (
  `ShippingAddressID` decimal(11,0) NOT NULL,
  `CustomerStreet` varchar(20) NOT NULL,
  `CustomerCity` varchar(20) NOT NULL,
  `CustomerState` char(2) NOT NULL,
  `CustomerZipCode` varchar(10) NOT NULL,
  `CustomerID` decimal(11,0) NOT NULL
);


INSERT INTO `shippingaddress_t` (`ShippingAddressID`, `CustomerStreet`, `CustomerCity`, `CustomerState`, `CustomerZipCode`, `CustomerID`) VALUES
('110', '123 Yale Avenue', 'Chicago', 'Il', '60066', '2220'),
('111', '144 Yale Avenue', 'Chicago', 'Il', '66666', '2220'),
('112', '123 Princeton Avenue', 'Chicago', 'Il', '60059', '1111'),
('113', '100 Forest Road', 'Oz', 'KS', '71234', '3330'),
('114', '110 Yale Avenue', 'Chicago', 'Il', '60066', '1111'),
('115', '220 Hale Avenue', 'Chicago', 'Il', '60066', '1111'),
('116', '333 Yellow Rd', 'Oz', 'KS', '72345', '3330');


CREATE TABLE `size_t` (
  `SizeID` decimal(2,0) NOT NULL,
  `Size` varchar(20) NOT NULL
);


INSERT INTO `size_t` (`SizeID`, `Size`) VALUES
('1', 'XS'),
('2', 'S'),
('3', 'M'),
('4', 'L'),
('5', 'XL');

INSERT INTO `orderline_t` (`OrderLineID`, `ProductQuantity`, `ProductID`, `OrderID`) VALUES
('1000', '2', '5', '101'),
('1001', '1', '3', '102'),
('1003', '1', '4', '104'),
('1004', '1', '5', '103'),
('1005', '1', '2', '102'),
('1006', '1', '3', '104');
