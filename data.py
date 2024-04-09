import sqlite3
ecom=sqlite3.connect("ecom.db")
n=["""CREATE TABLE `cart` (
  `p_id` int(10) NOT NULL,
  `c_email` varchar(256) NOT NULL,
  `quantity` int(10) NOT NULL DEFAULT 1,
  `sub_total` int(11) NOT NULL
);""","""
INSERT INTO `cart` (`p_id`, `c_email`, `quantity`, `sub_total`) VALUES
(24, 'dhanu@gmail.com', 1, 700),
(86, 'dhanu@gmail.com', 1, 560),
(10, 'varunvhns@gmail.com', 1, 5600),
(29, 'varunvhns@gmail.com', 1, 600),
(8, 'shiva@gmail.com', 2, 14200),
(37, 'shiva@gmail.com', 1, 2500),
(16, 'shiva@gmail.com', 1, 1600),
(50, 'hariharanrniit@gmail.com', 1, 2000);
""","""CREATE TABLE `category1` (
  `cat_id` int(11) NOT NULL,
  `cat_title` text NOT NULL
)""","""INSERT INTO `category1` (`cat_id`, `cat_title`) VALUES
(1, 'Furniture'),
(2, 'Bed'),
(3, 'Fountain'),
(4, 'Lighting');""","""CREATE TABLE `category2` (
  `cat_id` int(11) NOT NULL,
  `cat_title` text NOT NULL
)""","""
INSERT INTO `category2` (`cat_id`, `cat_title`) VALUES
(5, 'Flower'),
(6, 'Fruit'),
(7, 'Green Plant');""","""
CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL,
  `customer_name` text NOT NULL,
  `customer_email` varchar(255) NOT NULL,
  `customer_pass` varchar(255) NOT NULL,
  `customer_country` text NOT NULL,
  `customer_city` text NOT NULL,
  `customer_contact` varchar(255) NOT NULL,
  `customer_address` varchar(300) NOT NULL
);
""","""INSERT INTO `customers` (`customer_id`, `customer_name`, `customer_email`, `customer_pass`, `customer_country`, `customer_city`, `customer_contact`, `customer_address`) VALUES
(2, 'Ashok', 'ashok248@gmail.com', 'sample', 'India', 'Sivakasi', '8765113245', 'Mathang Kovil Street'),
(3, 'Dhanu', 'dhanu@gmail.com', 'sampledemo', 'India', 'Sivakasi', '8765113233', 'North Car Street '),
(4, 'varun', 'varunvhns@gmail.com', '12345', 'india', 'virudhunagar', '9023434343', '34 kk nagar, virudhunagar'),
(5, 'shiva', 'shiva@gmail.com', '12345', 'india', 'virudhunagar', '9023434333', '34  mani nagar');
""","""CREATE TABLE `ordered_products` (
  `sno` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
)
""","""
INSERT INTO `ordered_products` (`sno`, `order_id`, `customer_id`, `product_id`, `quantity`) VALUES
(1, 1, 2, 40, 1),
(2, 1, 2, 18, 1),
(3, 2, 3, 18, 1);
""","""CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `zip_code` int(10) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `address` varchar(300) NOT NULL,
  `total_price` int(11) NOT NULL
)
""","""INSERT INTO `orders` (`order_id`, `name`, `email`, `city`, `zip_code`, `mobile`, `address`, `total_price`) VALUES
(1, 'Ashok', 'ashok248@gmail.com', 'Sivaksi', 626123, '7654231234', 'Street', 4650),
(2, 'Dhanu', 'dhanu@gmail.com', 'Sivakasi', 626123, '7654231674', 'Mathang ', 2300);
""","""
CREATE TABLE `products` (
  `product_id` int(100) NOT NULL,
  `product_cat` text NOT NULL,
  `product_title` text NOT NULL,
  `product_price` int(100) NOT NULL,
  `product_desc` varchar(256) NOT NULL,
  `product_image` text NOT NULL,
  `product_keywords` text NOT NULL,
  `product_quantity` int(11) NOT NULL
)
""","""

INSERT INTO `products` (`product_id`, `product_cat`, `product_title`, `product_price`, `product_desc`, `product_image`, `product_keywords`, `product_quantity`) VALUES
(7, '1', 'Jelsy wood Furniture', 2700, 'Furniture made of Jelsy wood fully strong with Support Screws', 'lib.jpg', 'strong,wood,furniture,jelsy', 16),
(8, '1', 'Garden Furniture Teak Set ', 7100, 'Full set teak wood furniture set for garden use.', 'lin.jpg', 'furniture,garden,teak', 12),
(9, '1', 'Flexible belly Swing', 3800, 'Flexible belly Swing with push back for garden arrangement.', 'aahl.jpg', 'furniture,garden,belly,swing', 10),
(10, '1', 'Sandal wood Made Chair sets', 5600, 'This is a Chair set made of sandal wood with four chairs and one dining table. ', 'hih.jpg', 'chair,furniture', 13),
(11, '1', 'Cushion Chair set with table', 4600, 'This a chair set with high comfort cushion and table', 'gkjkj.jpg', 'furniture,garden,cushion', 4),
(12, '1', 'Thekar Echair', 6000, 'Thekar Echair with umbrella', 'ahs.jpg', 'furniture,garden,echair,umbrella', 12),
(14, '4', 'Craftter Textured Light', 1300, 'Craftter Textured Skyblue Round Wall Lamp (CRWL-51, blue) with serial pulses', 'Craftter Textured Skyblue Round Wall Lamp (CRWL-51, blue).jpg', 'light,wall,lamp', 15),
(16, '1', 'Stable Furniture with Table', 1600, 'Stable furniture with table set useful purpose for garden and park use.', 'jir.jpg', 'stable,furniture,set,garden', 13),
(17, '1', 'New Modern Garden Swing', 6000, 'Modern swing  for garden use and use to carry with wheels', 'hui.jpg', 'modern ,swing,garden,furniture,carry,wheels', 16),
(18, '4', 'Aesthetichs Double Glass Light', 2300, 'Aesthetichs Double Glass Chrome Finish Wall Light - 3094-1  Lamp Bright', 'Aesthetichs Double Glass Chrome Finish Wall Light - 3094-1.jpg', 'light,wall,lamp,glass', 11),
(19, '1', 'Wheel Shaped Fiber Chair', 1700, 'Wheel Shaped Fiber Chair for Garden use with a fiber table', 'wkih.jpg', 'fiber,chair,fiber,garden', 14),
(20, '1', 'Two chair with umbrella', 2500, 'Two chair with umbrella set fully with covered made of teak wood.', 'ahhh.jpg', 'Two chair with umbrella set fully with covered made of teak wood. furniture set', 11),
(21, '1', 'Well Comfort Swing', 3300, 'Well Comfort Swing useful for garden.', 'suj.jpg', 'Well Comfort Swing useful for garden. furniture', 7),
(22, '1', 'Party Chair Set', 5600, 'Party Chair set with dining table full white color ,made of fiber.', 'suhdi.jpg', 'Party Chair set with dining table full white color ,made of fiber. furniture', 14),
(23, '2', 'Ultra Soft Cushion Seat', 800, 'Ultra Soft Cushion Seat for garden chair as well as home use', '41D+X9ClDaL._AC_US160_.jpg', 'Ultra Soft Cushion Seat', 15),
(24, '2', 'Grey made Cushion', 700, 'Grey made Cushion seat for car chair..', '41HUKrtTcsL._AC_US160_.jpg', 'Grey made Cushion bed', 16),
(25, '2', 'Garden Matress', 2500, 'Well comfort Garden sleep matress', '41JT2m6lpvL._AC_US160_.jpg', 'Well comfort Garden sleep matress bed', 14),
(26, '2', 'Double Pillow Swing set', 1600, 'Double Pillow Swing set for garden Swing', '51Rn2GREz6L._AC_US160_.jpg', 'Double Pillow Swing set bed', 17),
(27, '2', 'Semi Folded Bed', 2300, 'Semi Folded Bed with curtain cushion', '516s6gKDjfL._AC_US160_.jpg', 'Semi Folded Bed ', 13),
(28, '2', 'Cushion chair', 1200, 'Cushion chair single garden set', '241277_R_Z001.jpg', 'Cushion chair bed', 14),
(29, '2', 'Single light Cushion', 600, 'Single light weight garden Cushion..with mile color ', 'garden-cushions.jpg', 'Single light Cushion bed', 15),
(31, '2', '6 set Pillows', 2400, 'Set of six bed pillows each of different color', 'index.jpg', 'Set of six bed pillows each of different color bed', 12),
(32, '2', 'Mixed color Cushion', 2300, 'Mixed color Cushion set for coupled Chairs', 'jjgg.jpg', 'Mixed color Cushion set for coupled Chairs bed', 16),
(33, '2', 'Fully Folded Cushion ', 800, 'Fully Folded Cushion completely north style...', 'Outdoor-Multicolored-Floral-Wicker-Seat-Cushions-Set-of-2-P14095781.jpg', 'Fully Folded Cushion completely north style... bed', 10),
(34, '2', 'Echair with Comfort Cushion', 1800, 'Echair with Comfort Cushion for garden', 'P1020889.jpg', 'Echair with Comfort Cushion for garden bed', 12),
(35, '3', 'Beauty Fountain ', 4000, 'Beauty Fountain for garden entrance', '392b4bab0db32d0c24f0e7feba7d7276.jpg', 'Beauty Fountain fountain', 15),
(36, '3', 'Ani made Fountain ', 2800, 'Ani made Fountain with silver streak', '110817gw-prateek-exports-original-imaep9fwevyrfwzt.jpeg', 'Ani made Fountain with silver streak Fountain', 13),
(37, '3', 'Stone Like Fountain', 2500, 'Stone Like Fountain for garden and house', '110829sr-prateek-exports-original-imaep9fzhxh59gyz.jpeg', 'Stone Like Fountain garden', 9),
(38, '3', 'Potted Fountain', 2000, 'Potted fountain with water reflector', 'ef4f26a31ce629fd0d5993df92f38c34.jpg', 'Potted Fountain ', 17),
(39, '3', 'Night Light Fountain', 4000, 'Night Light Fountain with bright handmade lights', 'garden_lights_online_shopping_in_india_5668_3200_3200.jpg', 'Night Light Fountain with bright handmade lights', 12),
(40, '3', 'Buddha Fountain', 2350, 'Well Portrait Buddha fountain with curly water curves', 'gw9851a-ufc-mart-original-imaehb3evfhy9sbh.jpeg', 'Well Portrait Buddha fountain with curly water curves', 12),
(41, '3', 'Rock Made Light Fountain', 2550, 'Rock Made Light Fountain with heavy beauty lights', 'gw11605-prateek-retail-original-imaenez8y4byrwuj.jpeg', 'Rock Made Light Fountain', 10),
(42, '3', 'Small Covered Light Fountain', 1550, 'Small Covered Light Fountain with tiny water pills', 'hggj.jpg', 'Small Covered Light Fountain with tiny water pills', 15),
(44, '3', 'Lamp Shaped Fountain', 4000, 'Lamp Shaped Fountain with water holes flow.', 'iyfufu.jpg', 'Lamp Shaped Fountain', 16),
(45, '3', 'Umbrel Fountain', 3000, 'Umbrel Fountain with man shaped portrait', 'luxus-szokkutak-kedvez-aron-.jpg', 'Umbrel Fountain with man shaped portrait', 12),
(46, '3', 'Outdoor Water Fountains', 2310, 'Outdoor-Water-Fountains-Decorative for garden', 'Outdoor-Water-Fountains-Decorative.jpg', 'Outdoor-Water-Fountain-Decorative for garden', 13),
(47, '2', 'Packed Bed', 800, 'Packed Bed For garden use cushion Comfort', 'packed.jpg', 'Packed Bed For garden use cushion Comfort', 15),
(48, '3', 'Jug Fountain', 4500, 'Jug Fountain with Three jugs', 'images.jpg', 'Jug Fountain with Three jugs', 12),
(49, '4', 'Rounded Light', 1500, 'Rounded bright light for garden ....', 'asas.jpg', 'Rounded bright light for garden ....', 16),
(50, '4', 'Candeberg 12 Flameless LED ', 2000, 'Candeberg 12 Flameless LED Tealight Candles- long lasting- 70+ hours each- thick designer paper wraps.Quality Guaranteed.', 'Candeberg 12 Flameless LED Tealight Candles- long lasting- 70+ hours each- thick designer paper wraps.Quality Guaranteed..jpg', 'Candeberg 12 Flameless LED Tealight Candles light', 13),
(51, '4', 'IFITech Solar Garden ', 1750, 'IFITech Solar Garden Designer Light - 2 Nights Working with 1 day Sun Charge', 'IFITech Solar Garden Designer Light - 2 Nights Working with 1 day Sun Charge.jpg', 'IFITech Solar Garden Designer Light - 2 Nights Working with 1 day Sun Charge light', 12),
(52, '4', 'OEM Outdoor Stainless ', 1500, 'OEM Outdoor Stainless Steel Waterproof LED Solar Garden Lights Landscape Lamps 5pcs Set', 'OEM Outdoor Stainless Steel Waterproof LED Solar Garden Lights Landscape Lamps 5pcs Set.jpg', 'OEM Outdoor Stainless Steel Waterproof LED Solar Garden Lights Landscape Lamps 5pcs Set', 16),
(53, '4', 'Outdoor-Solar-Power-3-LED-Bulbs', 1500, 'Outdoor-Solar-Power-3-LED-Bulbs-Light-Buried-Lamp-Path-Way-Garden-Under-Ground-Decking-Yard', 'Outdoor-Solar-Power-3-LED-Bulbs-Light-Buried-Lamp-Path-Way-Garden-Under-Ground-Decking-Yard.jpg', 'Outdoor-Solar-Power-3-LED-Bulbs-Light-Buried-Lamp-Path-Way-Garden-Under-Ground-Decking-Yard', 10),
(54, '4', 'Preyank Solar 10 X Solar ', 3050, 'Preyank Solar 10 X Solar Led Light For Path Garden Outdoor Landscape Yard Cool White Lamp', 'Preyank Solar 10 X Solar Led Light For Path Garden Outdoor Landscape Yard Cool White Lamp.jpg', 'Preyank Solar 10 X Solar Led Light For Path Garden Outdoor Landscape Yard Cool White Lamp', 13),
(55, '4', 'Quace Brand New Weatherproof ', 2360, 'Quace Brand New Weatherproof Solar Powered Deck Underground LED Lights Lamp Outdoor Garden Yard', 'Quace Brand New Weatherproof Solar Powered Deck Underground LED Lights Lamp Outdoor Garden Yard.jpg', 'Quace Brand New Weatherproof Solar Powered Deck Underground LED Lights Lamp Outdoor Garden Yard', 15),
(56, '4', 'Superscape Outdoor Lighting', 1300, 'Superscape Outdoor Lighting Gate Pillar Post Lighting GL4622', 'Superscape Outdoor Lighting Gate Pillar Post Lighting GL4622.jpg', 'Superscape Outdoor Lighting Gate Pillar Post Lighting GL4622', 12),
(57, '4', 'Tiny Deal 6-Led 18Lm Solar ', 1450, 'Tiny Deal 6-Led 18Lm Solar Powered Light Control Energy Saving Wall Lamp Road Lamp Garden Lamp - White', 'Tiny Deal 6-Led 18Lm Solar Powered Light Control Energy Saving Wall Lamp Road Lamp Garden Lamp - White.jpg', 'Tiny Deal 6-Led 18Lm Solar Powered Light Control Energy Saving Wall Lamp Road Lamp Garden Lamp - White', 17),
(58, '4', 'Waterproof LED Solar Garden', 1800, 'Waterproof LED Solar Garden Light Outdoor Landscape Stake Lamps Brand New Imported', 'Waterproof LED Solar Garden Light Outdoor Landscape Stake Lamps Brand New Imported.jpg', 'Waterproof LED Solar Garden Light Outdoor Landscape Stake Lamps Brand New Imported', 12),
(94, '1', 'Red Painted Chair', 300, 'Food with red cushion chair', '241277_R_Z001.jpg', 'red', 4);
"""]
#r=["cart","category1","category2","customers","ordered_products","orders","products"]
for k in n:
    try:
  
        #ecom.execute("drop table "+k)
        #ecom.execute(k)
        ecom.commit()
    except:
        pass

x=[k[0] for k in ecom.execute("select product_image from products").fetchall()]
print(x)
