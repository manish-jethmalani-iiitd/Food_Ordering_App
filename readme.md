# About The Project:
An online food ordering system accepts orders from customers and delivers at customer’s address. Items are selected from a menu and the total bill amount is calculated. Selected items may be put in a cart and addition, deletion of items in the cart is possible. Once the order is confirmed, the time taken for delivery is intimated and the order can be tracked. There are several payment modes, cash/wallet/bank transfer/credit/debit card on delivery or pre-paid. Orders placed may be cancelled if delivery time exceeds 10% of specified time.

## Features:
**Authentication:** 
* Sign up as new user/Login as existing user.
* Password Authentication and option to reenter password if entered wrong password.
* Option of sign up if user's details are not there in database while logging in.

**Order:**
* Accepts Customer's Location in the form of latitude and longitude coordinates.
* Displays the Restaurants.
* Displays the Menu of the Selected Restaurant which contains columns like Categoy, Item, Ratings and Price.

**Cart:**
* Add/Remove items in/from the cart.
* Add items from cart to the wishlist.
* Discard the Order.
* Displays items in the order.
* Go to payment section.

**Payment**:
* Displays total amount including delivery charges.
* Option to add promocode- Save50 and Save20.
* Payment options:\
Phone pay\
Google pay\
Netbanking\
Credit card\
Debit card

**Tracking**
* Displays estimated delivery time based on the distance of customer from the restaurant and preparation time of the restaurant.
* Option to cancel the order if delivery time exceeds 10% of estimated delivery time.
* Option to rate the app and food.

## Libraries required:
* sqlite3
* pandas
* geopy
* abc
* cProfile
* pstats
* io

## Instructions to run the Code:
* Keep the .db files in the directory.\
* Install the required libraries.\
* Enter input in the specified format and type as displayed in code and UML class diagram

## Doxygen file location:
* doxygen.html\html\index

## Video instruction:
* We missed one test case and added it later by merging the videos so kindly watch whole video.










