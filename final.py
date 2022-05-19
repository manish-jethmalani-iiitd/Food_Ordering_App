import sqlite3 as sql
import pandas as pd
import geopy.distance
from abc import ABC
conn1=sql.connect('coustemers2.db',timeout=10)
c1=conn1.cursor()
conn= sql.connect('order.db') #order is name of data base
#create a cursor named c
c=conn.cursor()
class db(ABC):
    '''Abstract class is implemented here as we need to read it in below classes'''
    def databa_det():
            '''used for reading the database'''
            
            df11 = pd.read_sql("select * from log_det", conn1)
                #read the data from databae to pandas dataframe
            res=[]
            for column in df11.columns:
                    
                li = df11[column].tolist()
                    #converts columns to list
                    
                res.append(li)
                    
            nam=res[0]
            mai=res[1]
            pasw=res[2]
            return nam,mai,pasw 
                #return the name,mail,password in the from of the list
class authe(db):
    """Used for authentication and signup and login and exception handling"""
    def _init_(self):
        db._init_(self)
    def check_table(self):
        try:
            c1.execute("""CREATE TABLE log_det (
                        name text unique,
                        email text unique,
                        password int
                        )""")
            print('excecution is done')
        except :
            print( 'table already exsists ')
    
    def signup(self,usern,mai,pas):
        """Used for signup"""
        #func to validate signup details
        self.usern=usern
        self.pas=pas
        self.mai=mai
        username1=usern
        paswo1=pas
        mail1=mai
        nam,mai1,pasw=db.databa_det() 
        #inheritance of db class to verify the data
        if usern in nam:
            print('user name already exsists')
            return False
        elif mai in mai1:
            print('user email alredy exsists')
            return False
        else:
            app_li=[(username1,mail1,paswo1)]
            #c1.execute("""INSERT INTO log_det VALUES(username1,mail1,paswo1)""")
        
            c1.executemany("INSERT INTO log_det VALUES(?,?,?)",app_li)
            
            
            conn1.commit()
            #conn1.close
            nam,mai1,pasw=db.databa_det()
            if usern in nam:
              if mai in mai1:
                print('user registered sucsessfully')
                return True



    def login(self,userna,passw):
        '''Used for login'''
        #function to validate login credentials
        self.userna=userna
        self.passw=passw
        usernam=userna
        paswo=passw
        #df11 = pd.read_sql("select * from log_det", conn1)
        
        nam,mai,pasw=db.databa_det()#inheritance of db class to verify the data
        k=-1
        r=-1
        for i in nam:
            r+=1
            if i==usernam:
                k=4
        if k==4:
            if pasw[r]==paswo:
                print('user is  able to login sucsessfully')
                return 1
            else:
                print('ask user to enter correct password')  
                return 2
        else:
            print('Ask user to signup')
            return 3

    def  authe_login(self,rm1) :
        '''Used for authentication by verifying login and signup''' 
        self.rm1=rm1
        rm=rm1
        #rm=int(input('select the option'))
            #re=authe() 
        if rm==1:
            
            username1=input('Enter Username:')
            emai=input('Enter email address:')
            pas=int(input('enter your password '))
            kre=authe.signup(self,username1,emai,pas)
            ireg=1
            while not kre and ireg==1:
                ireg=int(input('Enter 1 if you want to register or else 2'))
                while ireg==1:
                    username1=input('Enter Username:')
                    emai=input('Enter email address:')
                    pas=int(input('enter your password '))
                    kre=authe.signup(self,username1,emai,pas)
                    conn1.commit()
                    if kre:
                        ireg=2
            else:
                username2=input('Enter Registered Username:')
                pas2=int(input('enter your  password '))
                kre2=authe.login(self,username2,pas2)
                #print(kre2)
                co=0
                while kre2==2 and co<3:
                    co+=1
                    pas2=int(input('enter your  password  again'))
                    kre2=authe.login(self,username2,pas2)
                    if co==3:
                        print('User has exceede maximum limit please try after sometime')
                if kre2==3 :
                    username1=input('Enter Username:')
                    emai=input('Enter email address:')
                    pas=int(input('enter your password '))
                    kre=authe.signup(self,username1,emai,pas)
                    while not kre:
                        username1=input('Enter Username:')
                        emai=input('Enter email address:')
                        pas=int(input('enter your password '))
                        kre=authe.signup(self,username1,emai,pas)
                    
                if kre2==1 :
                  return 4
        elif rm==2:
                username2=input('Enter Registered Username:')
                pas2=int(input('enter your  password '))
                kre2=authe.login(self,username2,pas2)
                #print(kre2)
                co=0
                while kre2==2 and co<3:
                    co+=1
                    pas2=int(input('enter your  password  again'))
                    kre2=authe.login(self,username2,pas2)
                    if co==3:
                        print('User has exceede maximum limit please try after sometime')
                if kre2==3 :
                    username1=input('Enter Username:')
                    emai=input('Enter email address:')
                    pas=int(input('enter your password '))
                    kre=authe.signup(self,username1,emai,pas)
                    while not kre:
                        username1=input('Enter Username:')
                        emai=input('Enter email address:')
                        pas=int(input('enter your password '))
                        kre=authe.signup(self,username1,emai,pas)
                    else:
                      username2=input('Enter Registered Username:')
                      pas2=int(input('enter your  password '))
                      kre2=authe.login(self,username2,pas2)  
                if kre2==1 :
                    return 4
        elif rm==3:
                exit
class restaurant:
    '''To display menu,calculate distance and delivery time.Encapsulation is used here'''
    def __init__(self,res_num,lat,lon):
        self.__res_num=res_num
        self.__lat=lat
        self.__lon=lon
    def setres_num(self, res_num):
        '''setter function for restaurant number'''
        self.__res_num = res_num
    def setlat(self, lat):
        ''' setter function  for latitude'''
        self.__lat = lat
    def setlon(self, lon):
        ''' setter function for longitude'''
        self.__lon = lon
    def getres_num(self):
        ''' getter function for restaurant number'''
        return self.__res_num
    def getlat(self):
        '''getter function for latitude'''
        return self.__lat
    def getlon(self):
        '''getter function for longitude'''
        return self.__lon
    def display_menu(self):
        '''function to display menu'''
        df_menu0=pd.read_sql_query("SELECT * FROM menu0", conn)
        df_menu1=pd.read_sql_query("SELECT * FROM menu1", conn)
        df_menu2=pd.read_sql_query("SELECT * FROM menu2", conn)
        df_menu3=pd.read_sql_query("SELECT * FROM menu3", conn)
        df_menu4=pd.read_sql_query("SELECT * FROM menu4", conn)
        df_menu5=pd.read_sql_query("SELECT * FROM menu5", conn)
        df_menu6=pd.read_sql_query("SELECT * FROM menu6", conn)
        df_menu7=pd.read_sql_query("SELECT * FROM menu7", conn)
        menu_list=[df_menu0,df_menu1,df_menu2,df_menu3,df_menu4,df_menu5,df_menu6,df_menu7]
        print(menu_list[restaurant.getres_num(self)])
    def calculate_distance(self):
        '''function to calculate distance'''
        #self.lat=lat
        #self.lon=lon
        c.execute("SELECT * FROM {} WHERE rowid={}".format("restaurants",res_num + 1))
        res_lat=c.fetchone()[3]
        c.execute("SELECT * FROM {} WHERE rowid={}".format("restaurants",res_num + 1))
        res_lon=c.fetchone()[4]
        return geopy.distance.distance((lat,lon), (res_lat,res_lon)).km 
    def calculate_deltime(self,distance):
        '''function to calculate delivery time'''
        return 15 + distance*5  # 15 minutes preparation time . 5 minutes for each kilometer.
        
class cart(restaurant):
    '''To add/remove/discard items from cart and show items currently in cart.cart class inherits restaurant class'''
    def __init__(self):
        restaurant.__init__(self,res_num,lat,lon) 
    
    def show_order(self,order_list):
        '''Shows items currently in cart'''
        menu_table=["menu0","menu1","menu2","menu3","menu4","menu5","menu6","menu7"]
        temp=[]
        for i in range(len(order_list)):
            c.execute("SELECT * FROM {} WHERE rowid={}".format(menu_table[res_num],order_list[i]+1))
            temp.append(c.fetchone())
        tempdf=pd.DataFrame(temp,columns =['Category', 'Item', 'Ratings','Total_Price'])
        tempdf['Quantity']=1
        print(tempdf)
        tempdffinal=tempdf.drop(['Ratings','Category'],axis=1).groupby(['Item']).sum()
        tempdffinal= tempdffinal[['Quantity', 'Total_Price']] #rearranging columns
        print(tempdffinal)
        return temp

    def take_order(self):
        '''Function to add/remove/discard items from cart and add items from cart to wishlist.'''
        cart_input=6
        order_dict=dict()
        while(cart_input!=3):
            cart_input=int(input("Enter choice\n1.Add item into cart\n2.Remove an item from cart\n3.Go to payment section\n4.Add to Wishlist\n5.Discard the order\n"))
            if(cart_input==1):
                key,value=100,100
                while(key>=0 and value>=0):
                    key,value=input("Enter sr no. of item and quantity(SPACE SEPARATED) to add particular item in cart.Exit by entering negative integers\n").split()
                    key,value=int(key),int(value)
                    if(key<0 and value<0):
                        cart_input=6
                        order_list=[]
                        for keys in order_dict.keys():
                            for i in range(order_dict[keys]):
                                order_list.append(keys)
                        cart_obj.show_order(order_list)
                        break
                    order_dict[key]=value
            elif(cart_input==2):
                key,value=100,100
                while(key>=0 and value>=0):
                    key,value=input("Enter sr no. of item to remove particular item in cart.Exit by entering negative integers\n").split()
                    key,value=int(key),int(value)
                    if(key<0 and value<0):
                        cart_input=6
                        order_list=[]
                        for keys in order_dict.keys():
                            for i in range(order_dict[keys]):
                                order_list.append(keys)
                        cart_obj.show_order(order_list)
                        break
                    order_dict[key]=order_dict[key]-value
            elif(cart_input==4):
                print("Items are added to wishlist\n")
                cart_input=6
                order_list=[]
                for keys in order_dict.keys():
                    for i in range(order_dict[keys]):
                        order_list.append(keys)
                cart_obj.show_order(order_list)
            elif(cart_input==5):
                print("Order Discarded.Thank you for choosing Food Mart.")
                exit()
        order_list=[]
        for keys in order_dict.keys():
            for i in range(order_dict[keys]):
                order_list.append(keys)
        return order_list 
class payment(cart):
    '''To calculate total bill and receive payment. It inherits cart class'''
    def __init__(self):
        restaurant.__init__(self,res_num,lat,lon)
        cart.__init__(self)
    def payment_options(self,total):
        '''Function to receive payment'''
        print("""How would you like to pay?
        1.Phone pay
        2.Google pay
        3.Netbanking
        4.Credit card
        5.debit card""")
        p=int(input())
        if(p==1):
            q=int(input("enter your phonepay id:"))
            r=int(input("enter password:"))
            print(("Successfully debited rupees {} from your account.").format(total))
            #print(("Expected delivery time : {}").format(restaurant.calculate_deltime(self,distance)))
        elif(p==2):
            q=int(input("enter your googlepay id:"))
            r=int(input("enter password:"))
            print(("Successfully debited rupees {} from your account.").format(total))
            #print(("Expected delivery time : {}").format(restaurant.calculate_deltime(self,distance)))
        elif(p==3):
            q=int(input("enter your netbanking id:"))
            r=int(input("enter password:"))
            print(("Successfully debited rupees {} from your account.").format(total))
            #print(("Expected delivery time : {}").format(restaurant.calculate_deltime(self,distance)))
        elif(p==4):
            q=int(input("enter your creditcard number:"))
            r=int(input("enter password:"))
            print(("Successfully debited rupees {} from your account.").format(total))
            #print(("Expected delivery time : {}").format(restaurant.calculate_deltime(self,distance)))
        elif(p==5):
            q=int(input("enter your debitcard number:"))
            r=int(input("enter password:"))
            print(("Successfully debited rupees {} from your account.").format(total))
            #print(("Expected delivery time : {}").format(restaurant.calculate_deltime(self,distance)))
        else:
            print("not a valid option.")
    
    
    def pay_ment(self,order_list):
        '''Calculates total bill and displays the promo codes available'''
        #cart_obj=cart()
        #order_list=cart_obj.take_order()
        #order_list=[('Chaat Street', 'Pani Puri', 4.1, 60), ('Chaat Street', 'Raj Kachori', 4.1, 150), ('Chaat Street', 'Raj Kachori', 4.1, 150), ('Sandwiches and Pasta', 'Pasta In Cheese Sauce', 4.4, 200), ('Sandwiches and Pasta', 'Pasta In Cheese Sauce', 4.4, 200)]
        i=u=""
        total=0
        for i in order_list:
            total=total+i[3]
        #print("your total bill is:",total)
    
        #res_obj=restaurant(res_num)
        d1=restaurant.calculate_distance(self)
        delivery_charges=d1*5  #rupees 5/km
    
        print("delivery charges are:",delivery_charges)
    
        if total>100:
            print("your order is successfully placed.")
            print("Save50 and Save20 promo codes are available on this order.do you want to use promo code?(Y/N)")
            i=input()
            if(i=="Y"):
                print("which code you would like to use?")
                u=input()
                if (u=="Save50"):
                    total=total/2  #50% discount
                    total=total+delivery_charges
                    print("total bill after applying coupon code is:",total)
                    payment.payment_options(self,total)
                else:
                    total=total-total*0.2  #20% discount
                    total=total+delivery_charges
                    print("total bill after applying coupon code is:",total)
                    payment.payment_options(self,total)
            else:
                total=total+delivery_charges
                print("total bill after applying coupon code is:",total)
                payment.payment_options(self,total)
    
        else:
            print("We are sorry that we will not be able to take your order as it is below 100 rupees.")
            exit()
class track_order(restaurant):
    '''To track the order. It inherits restaurant class'''
    def __init__(self):
        restaurant.__init__(self,res_num,lat,lon)
    def tracking(self):
        '''Tracks the order and provides option to cancel if delivery time exceeds 10% more than estimated time'''
        distance=restaurant.calculate_distance(self)
        est_del_time=restaurant.calculate_deltime(self,distance)
        print(("Expected delivery time : {}").format(est_del_time))
        elapsed_time=int(input("Enter Elapsed Time : "))
        if(elapsed_time<1.10*est_del_time):
            print(("Your order will be delivered in {} minutes").format(est_del_time-int(elapsed_time)))
            print("Order Delivered.Enjoy your meal")
            food_rate=int(input("Please rate the food(1-5) : "))
            app_rate=int(input("Please rate the app(1-5) : "))
            print("Thanks for the feedback")
        else:
            x=input(("Do you want to cancel your order? Y/N "))
            if x=="Y":
                print("Order Cancelled.Thanks for choosing Food Mart.")
            else:
                print("Sorry for the delay.Your order is on the way and will be delivered soon")
                print("Order Delivered.Enjoy your meal")
                food_rate=int(input("Please rate the food(1-5) : "))
                app_rate=int(input("Please rate the app(1-5) : "))
                print("Thanks for the feedback")
if __name__=="__main__":
    import cProfile,pstats
    profiler = cProfile.Profile()
    profiler.enable()
    auth_obj=authe()
    auth_obj.check_table()
    print('''Welcome To the foodmart:
    Please select your option:
    1. New User
    2. Existing user
    3. Exit''')
    rm=int(input('select the option : ')) 
    l1=auth_obj.authe_login(rm)
    df_rest = pd.read_sql_query("SELECT * FROM restaurants", conn)
    print(df_rest)
    lat=float(input("Enter Your Latitude: "))
    lon=float(input("Enter Your Longitude: "))
    res_num=int(input("Select the Restaurant : "))
    res_obj=restaurant(0,0,0)
    res_obj.setres_num(res_num)
    res_obj.setlat(lat)
    res_obj.setlon=(lon)
    print(("Distance from Restaurant: {} km.").format(res_obj.calculate_distance()))
    distance=res_obj.calculate_distance()
    res_obj.display_menu()
    cart_obj=cart()
    order_list=cart_obj.take_order()
    temp=cart_obj.show_order(order_list)
    pay_obj=payment()
    pay_obj.pay_ment(temp)
    track_obj=track_order()
    track_obj.tracking()
    import io
    profiler.disable()
    s = io.StringIO()
    stats = pstats.Stats(profiler,stream=s).sort_stats('ncalls')
    stats.print_stats()
    with open('test.txt', 'w+') as f:
        f.write(s.getvalue())