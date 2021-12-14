IINSERT INTO billingaddress_t (BillingAddressID, CustomerStreet, CustomerCity, CustomerState, CustomerZipCode, id) VALUES
(1, 100 Forest Road, Oz, KS, 71234, 3330),
(2, 144 Yale Avenue, Chicago, IL, 66666, 1111),
(3, 123 Harvard Avenue, Chicago, IL, 66770, 2220),
(5, 333 Yellow Rd, Oz, KS, 71234, 3330);

INSERT INTO category_t (CategoryID, CategoryType) VALUES
(1, Skirt),
(2, Shirt),
(3, Dress),
(4, Pants),
(5, Sweater);

INSERT INTO color_t (ColorID, Color) VALUES
(1, Red),
(2, Blue),
(3, Green),
(4, Yellow),
(5, White),
(6, Black),
(7, Orange),
(8, Purple);


INSERT INTO customer_t (id, CustomerName, CustomerPhoneNumber, username, email, image_file, password) VALUES
(3, Tom Thumb, 12345678901, tthumb, tthumb@test, default.jpg, 12345),
(1111, Alex Jones, 2345678910, ajones, aj@test, default.jpg, 12345),
(2220, Jane Smith, 9999999999, jsmtih, jane@test, default.jpg, 12345),
(3330, Ali Fang, 8890000000, afang, afang@test, default.jpg, 12345);

INSERT INTO orderline_t (OrderLineID, ProductQuantity, ProductID, OrderID) VALUES
(1000, 2, 5, 101),
(1001, 1, 3, 102),
(1003, 1, 4, 104),
(1004, 1, 5, 103),
(1005, 1, 2, 102),
(1006, 1, 3, 104),
(1009, 1, 1, 107);

INSERT INTO order_t (OrderID, OrderDate, OrderStatus, id) VALUES
(101, 2021-12-04 06:33:19, Completed, 3330),
(102, 2021-12-04 06:33:19, Processing, 2220),
(103, 2021-12-04 06:34:15, Shipped, 2220),
(104, 2021-12-04 06:34:15, Processing, 1111),
(107, 2021-12-13 07:17:41, Processing, 3);

INSERT INTO product_t (ProductID, ProductDescription, ProductSize, ProductPrice, ProductColor, ProductAvailableQuantity, ProductSKUCode, ProductImageFileName, CategoryID, ColorID, SizeID) VALUES
(1, High-waisted mini skirt with elastic waistband., S, 50.25, Blue, 15, 123456, Image01, 1, 2, 2),
(2, Mid-rise pants with side pockets and back false welt pockets. Front zip, metal hook, and interior button closure., M, 45.90, Blue, 15, 159753, Image02, 4, 2, 3),
(3, Petite recycled lace trim long sleeve mini dress, L, 20.20, Blue, 15, 165412, Image03, 3, 2, 4),
(4, Strap detail slip dress, S, 74.00, Yellow, 15, 147258, Image04, 3, 4, 2),
(5, Full cut round neck sleeveless top, M, 85.89, Black, 15, 258369, Image05, 2, 6, 3);

INSERT INTO shippingaddress_t (ShippingAddressID, CustomerStreet, CustomerCity, CustomerState, CustomerZipCode, id) VALUES
(110, 123 Yale Avenue, Chicago, Il, 60066, 2220),
(111, 144 Yale Avenue, Chicago, Il, 66666, 2220),
(112, 123 Princeton Avenue, Chicago, Il, 60059, 1111),
(113, 100 Forest Road, Oz, KS, 71234, 3330),
(114, 110 Yale Avenue, Chicago, Il, 60066, 1111),
(115, 220 Hale Avenue, Chicago, Il, 60066, 1111),
(116, 333 Yellow Rd, Oz, KS, 72345, 3330);

INSERT INTO size_t (SizeID, Size) VALUES
(1, XS),
(2, S),
(3, M),
(4, L),
(5, XL);






