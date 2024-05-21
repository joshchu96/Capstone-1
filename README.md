API: cocktailDB
URL: https://www.thecocktaildb.com/api.php


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

Cocktail Recipe App
This web application is a Cocktail Recipe App that is designed to help users find and save cocktail recipes. Users are able to search the cocktails by name, look at their detailed information, register an account, login, and save their favorite cocktails in a personalized list. 

Features
User registration and authentication are implemented using Flask-WTF for form handling and SQL-Alchemy for managing the database. These features allowed the users to create and log in to secure accounts. 
Users can search for cocktails by inputting cocktail names in the search functionality. The app integrates with an external API(cocktailDB) to fetch the data based on user input. 
Users can also view detailed information regarding the cocktail(image, ingredients, and instructions for preparing the cocktail).
User Profile: Registered users have a profile page where they can view their saved cocktail recipes. The user can also remove cocktails from their profile if they desire.
Liking Cocktails: Users can save cocktails to their registered profiles for easier access in the future. Liked cocktails will be displayed on the user's profile page. 

User Flow
Registration: Users can navigate the registration page and fill out the register form with their desired username, password, first name, and last name. 
When registration is successful, the user will be redirected to the login page. 

Login
Registered users can log in using their username and password. 
Passwords are encrypted using Flask-bcrypt and will be authenticated to previously stored user information. 
Upon successful login, the user will be redirected to their profile page. 

Search Cocktails
Users can navigate the search page for cocktails by name. 
Users enter the name of the cocktail they are looking for and submit the form.
If the cocktail matching in the search query is found, a list of matching cocktails is displayed. If the query returns none, an error message will be displayed. 

View Cocktails
Users can click on the cocktail in the search results to view detailed information about each cocktail.
Detailed information includes (image, ingredients, and instructions for preparation.

Like Cocktails
When navigating the detailed information about the cocktail, users have the option to like & save the cocktail to their own personalized profiles. 
Liked cocktails are stored as a list format in the user's profile for future reference.

User Profile
The profile page will display the user's information along with a list of liked cocktails. 

Logout
Users can lock out of their account by clicking the "Logout" button in the navigation bar under the list of personal cocktails their liked. 
Upon logging out the user will be redirected to the login page. 

API
The API used in this application to fetch cocktail data based on user input is CocktailDB. The API provides endpoints for search cocktails by name and retrieving detailed information regarding specific cocktails. 

Technology Stack
Frontend: HTML, CSS, Bootstrap
Backend: Python, Flask
Database: PostgreSQL, SQLAlchemy
API Integration: Flask(requests)
Others: Flask-WTForms, Flask-DebugToolbar(for debugging purposes during development)

Final Notes
The application uses Flask's session management to keep track of users authentication and authorization for certain methods. 
Remember to keep the API keys and any sensitive information secure by placing them in a separate file.








