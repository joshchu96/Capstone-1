
Database Schema 
Crows Foot Diagram

USER
Id: primarykey
Username: text,notnull,unique
password:text,notnull
first_name:text,notnull
last_name:text,notnull 



USER_LIKES_DRINKS
Id: primarykey
User_id: ForeignKey
Drink_id: ForeignKey




Drinks
Id: primarykey
Name: text, notnull
Description: text
Image_url: text




Relationships

USER.id ( one —-----------------------> many ) USER_LIKES_DRINKS.user_id

USER_LIKES_DRINKS.drink_id (many ←—---------------- one ) Drinks.id

1 User can like many Drinks. 
1 Drink can be liked by many Users. 
This schema shows an association table (USER_LIKES_DRINKS) that is linked by adjacent tables (USERS) && (DRINKS).
