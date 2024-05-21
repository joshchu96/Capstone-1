
Database Schema 
Crows Foot Diagram

USER
Id: primarykey
Username: text,notnull,unique
password:text,notnull
first_name:text,notnull
last_name:text,notnull 


LikedCocktail
Id: primarykey
user_id: Integer, Foreignkey(user.id) not null
cocktail_name: String not null
user = relationship 'USER' backref='liked_cocktails





