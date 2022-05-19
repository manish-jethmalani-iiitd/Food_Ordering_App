import sqlite3
import pandas as pd
import geopy.distance
conn= sqlite3.connect('order.db') #order is name of data base
#create a cursor named c
c=conn.cursor()
#create a table
c.execute("""CREATE TABLE restaurants(
    res_name text,
    cusine text,
    ratings real,
    latitude real,
    longitude real
)
""")
def create_menutable(x):    
    c.execute(("""CREATE TABLE {}(
    category text,
    item text,
    ratings real,
    price int
    )
    """).format(x))
    conn.commit()
create_menutable("menu0")
create_menutable("menu1")
create_menutable("menu2")
create_menutable("menu3")
create_menutable("menu4")
create_menutable("menu5")
create_menutable("menu6")
create_menutable("menu7")
def show_table(x):
    c.execute(("SELECT rowid, * FROM {}").format(x))
    items=c.fetchall()
    for item in items:
        print(item)
many_rest=[
                ('Mehak Food Corner','North Indian',4.1,28.544086525111467, 77.25092189552106),
                ("Nirula's",'Icecream and Beverages',4.6,28.54023872840331, 77.2404012689296),
                ('VIP SWEETS','Sweets',3.9,28.537209777041813, 77.25300389622915),
                ('Tandoor N Grills','North Indian',3.3,28.568160009745835, 77.28131583273098),
                ('Havmor Havfunn','Icecream',4.5,28.542867225744875, 77.25253840759102),
                ('Anna Ka Dosa','South Indian',3.9,28.541937077887823, 77.25530836439867),
                ('Wrap It Up!','Mexican and Lebanese',4.0,28.540794387482286, 77.25700220586603),
                ("Haldiram's",'North Indian,Sweets,Namkeen and Snacks',4.4,28.539166110568004, 77.25924391238627),
]
c.executemany("INSERT INTO restaurants VALUES (?,?,?,?,?)",many_rest)
conn.commit()
many_menu0=[
                ('Thalis','Choor Choor Naan Thali',4.2,130),
                ('Thalis','Amritsari Naan Thali',4.5,110),
                ("Meals",'Rajma Rice',4.4,75),
                ("Meals",'Dal Makhani Rice',4.1,75),
                ("Meals",'Shahi Paneer Rice',4.0,90),
                ("Meals",'Chole Rice',4.6,75),
                ('Specials','Gulab Jamun (1pc)',3.9,25),
                ('Specials','Jalebi',4.5,30),
                ('Specials','Chole Bature',4.9,80),
                ('Specials','Moong Dal Samosa',3.8,20),
                ('Specials','Allu ka Samosa',3.9,14),
                ('Main Course','Shahi Paneer',4.1,140),
                ('Main Course','Rajma',4.5,70),
                ('Main Course','Kadhi Rice',3.7,70),
                ('Main Course','Kadhi Pakora',3.5,70),
                ('Main Course','Chole',4.2,45),
                ('Main Course','Dal Makhani',3.3,120),
                ('Main Course','Plain Rice',3.7,40),
                ('Main Course','Paneer Stuff Naan',4.1,35),
                ('Main Course','Aloo Stuff Naan',4.0,30),
                ('Main Course','Paneer Stuff Bhature',4.0,20),
                ('Main Course','Tawa Roti',3.8,7),
                ('Accompanient','Raita(100ml)',3.9,35),
                
]
c.executemany("INSERT INTO menu0 VALUES (?,?,?,?)",many_menu0)
conn.commit()
many_menu1=[
                ('Winter Specials','Roasted Almonds',4.0,77),
                ('Winter Specials','Fig and Honey',3.9,80),
                ('Winter Specials','Hazelnut Crunch',4.2,85),
                ('Icecream Cakes','Chocolate Chip IceCream Cake',4.5,750),
                ("Icecream Tubs",'Alpha Mango Tub',4.2,340),
                ("Icecream Tubs",'Vanilla Tub',4.3,300),
                ("Icecream Tubs",'Strawberry Cheese Tub',4.0,340),
                ("Icecream Tubs",'Coffee Walnut Brownie Tub',4.5,345),
                ("Icecream Tubs",'Pineapple Pop Tub',4.4,300),
                ("Icecream Tubs",'Tooti Frooti Tub',4.0,320),
                ("Icecream Cones",'Waffle Cone',4.1,25),
                ("Icecream Cones",'Waffle Cone Black',3.9,25),
                ("Icecream Sodas & and Beverages",'Double Chocolate Icecream Soda',4.1,135),
                ("Icecream Sodas & and Beverages",'Golden Glow',4.0,135),
                ("Icecream Sodas & and Beverages",'Lime Ice',4.2,135),
                ("Icecream Sodas & and Beverages",'Strawberry Icecream Soda',4.0,135),
                ("Shakes",'Vanilla Milkshake',4.6,135),
                ("Shakes",'Butter Scotch Milkshake',4.3,135),
                ("Shakes",'Chocolate Milkshake',4.6,135),
                ("Shakes",'Cold Coffee',4.7,135),
                ("Shakes",'Kitkat Milkshake',4.4,175),
                ('Scoops','Red Velvet',3.9,65),
                ('Scoops','Choco Rocks ',4.0,60),
                ('Scoops','21 Love',4.5,80),
                ('Scoops','Vanilla',4.7,70),
                                
]
c.executemany("INSERT INTO menu1 VALUES (?,?,?,?)",many_menu1)
conn.commit()
many_menu2=[
                ('Sweets','Jalebi 1 kg',4.1,280),
                ('Sweets','Emirati 1 kg',4.0,340),
                ('Sweets','Rasmalai 1 pc',4.2,35),
                ('Sweets','Sponge Rasgulla 1 pc',4.0,30),
                ('Sweets','Gulab Jamun 1 pc',4.1,16),
                ('Sweets','Motichoor Laddu 1 kg',3.8,380),
                ('Sweets','Besan Laddu 1 kg',4.0,320),
                ('Sweets','Rasgulla 1 kg',4.0,380),
                ('Sweets','Gulab Jamun 1 kg',4.1,380),
                ('Sweets','Cham Cham 1 kg',4.0,520),
                ('Sweets','Malai Chaap 1 kg',4.1,520),
                ('Sweets','Chhena Toast 1 kg',3.9,520),
                ('Sweets','Plain Barfi 1 kg',4.0,520),               
]
c.executemany("INSERT INTO menu2 VALUES (?,?,?,?)",many_menu2)
conn.commit()
many_menu3=[
                ('Breakfast and Lunch','Chole Bhature',4.1,60),
                ('Breakfast and Lunch','Chole Chawal',4.0,60),
                ('Breakfast and Lunch','Boondi Raita',4.1,30),
                ('Starters','Paneer Tikka',4.0,120),
                ('Starters','Paneer Malai Tikka',4.2,130),
                ('Starters','Malai Chaap',4.0,140),
                ('Starters','Afghani Chaap',4.2,135),
                ('Rolls','Soya Tikka Roll',4.1,80),
                ('Rolls','Chicken Seekh Roll',4.3,100),
                ('Rolls','Chicken Tikka Roll',4.2,100),
                ('Rolls','Paneer Roll',4.0,90),
                ('Breads','Butter Naan',4.1,30),
                ('Breads','Butter Roti',4.0,40),
                ('Breads','Rumali Roti',4.2,20),
                ('Breads','Tandoori Roti',4.3,20),
                               
]
c.executemany("INSERT INTO menu3 VALUES (?,?,?,?)",many_menu3)
conn.commit()
many_menu4=[
                ('Icecream Cake','Blackforest Icecream Cake Slice',4.1,100),
                ('Icecream Cake','Chocolate Carnival Cake',4.2,750),
                ('Icecream Cake','Strawberry Cheese Cake',4.0,700),
                ('Loose Ice Cream','Black Current 500gm',4.0,350),
                ('Loose Ice Cream','Cookie Cream 500gm',4.3,380),
                ('Loose Ice Cream','Vanilla 500gm',4.1,240),
                ('Scoops','Butter Scotch Scoop',4.1,125),
                ('Scoops','Chocolate Chips',4.3,130),
                ('Scoops','Red Velvet',4.1,130),
                ('Sundaes','Oreo Loaded',4.0,150),
                ('Sundaes','Choco Carnival Wonder',4.2,110),
                ('Sundaes','Fruit Overload',3.5,120),
                ('#Mor2Go','Death By Chocolate',4.2,850),
                ('#Mor2Go','Sugarfree Premium Vanilla',4.0,230),
                ('#Mor2Go','Mango Cheesecake',4.2,250),                             
]
c.executemany("INSERT INTO menu4 VALUES (?,?,?,?)",many_menu4)
conn.commit()
many_menu5=[
                ('Idli and Vada','Idli Sambhar 1 pc',4.1,50),
                ('Idli and Vada','Idli Sambhar 1 pc',4.1,80),
                ('Idli and Vada','Vada Sambhar 1 pc',4.0,50),
                ('Dosas','Masala Dosa',4.5,140),
                ('Dosas','Mysore Masala Dosa',4.2,160),
                ('Dosas','Cheese Masala Dosa',4.3,200),
                ('Rice','Curd Rice',4.0,80),
                ('Rice','Upma',3.8,90),
                ('Rice','Lemon Rice',3.5,70),
                ('Uttapams','Onion Uttapams',4.0,150),
                ('Uttapams','Paneer Uttapams',4.2,180),
                ('Uttapams','Mix Veg Uttapams',4.0,160),
                ('Desserts','Kesar Halwa',4.3,60),
]
c.executemany("INSERT INTO menu5 VALUES (?,?,?,?)",many_menu5)
conn.commit()
many_menu6=[
                ('Veg Burgers','Mexican Veg Burger',4.1,230),
                ('Veg Burgers','Lebanese Falafel Burger',4.4,230),
                ('Non Veg Burgers','Mexican Chicken Burger',4.1,250),
                ('Non Veg Burgers','Lebanese Mutton Burger',4.3,260),
                ('Veg Wraps','Spicy Paneer Wrap ',4.0,240),
                ('Veg Wraps','Chili Chinese',4.0,230),
                ('NonVeg Wraps','Chinese Chicken Wrap',4.5,280),
                ('NonVeg Wraps','Chicken Tikka Wrap',4.3,290),
                ('Sides','French Fries',4.3,100),
                ('Sides','Kebab Box',4.4,150),
                ('Beverages','Cold Coffee',4.0,130),
                ('Beverages','Oreo Milkshake',4.5,160),
]
c.executemany("INSERT INTO menu6 VALUES (?,?,?,?)",many_menu6)
conn.commit()
many_menu7=[
                ('Chaat Street','Pani Puri',4.1,60),
                ('Chaat Street','Raj Kachori',4.1,150),
                ('Sandwiches and Pasta','Pasta In Cheese Sauce',4.4,200),
                ('Sandwiches and Pasta','Grilled Sandwich With Chips',4.1,180),
                ('Rice Bowls','Mix Veg Rice Combo',4.1,155),
                ('Rice Bowls','Dal Makhani With Rice',4.0,150),
                ('Breads','Aloo Paratha',4.3,100),
                ('Breads','Paneer Kulcha',4.3,110),
                ('Chinese','Noodles',4.0,200),
                ('Chinese','Paneer Chilli ',4.2,250),
                ('Dry Fruits','Badam',4.0,380),
                ('Dry Fruits','Roasted Badam',4.5,600),
                ('Sweets','Soan Cake 500 gm',4.5,200),
                ('Sweets','Chocolate Barfi 1 kg',4.7,600),

]
c.executemany("INSERT INTO menu7 VALUES (?,?,?,?)",many_menu7)
conn.commit()