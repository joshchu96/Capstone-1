from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from api import search_name
from models import db, connect_db, User, LikedCocktail
from forms import LoginForm, RegisterForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///recipe-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True

connect_db(app)
app.app_context().push()
db.create_all()

app.config['SECRET_KEY']='shhh'
toolbar = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """Homepage for drink app"""
    return render_template('home.html')

@app.route("/search", methods=["GET","POST"])
def search_cocktail():
    """Search for the drink by name"""
    search_input = request.form.get('search-form')
    data = search_name(search_input)
    if data['drinks']:
        cocktail_list = [cocktail['strDrink'] for cocktail in data['drinks']]
        return render_template("display_cocktail.html", cocktail_list=cocktail_list)
    else:
        return render_template('error.html')

@app.route("/display_<cocktail_name>/info")
def cocktail_details(cocktail_name):
    """Display detailed info on cocktail"""
    #grab the image url
    data = search_name(cocktail_name)
    drink = data['drinks'][0]
    image = drink.get('strDrinkThumb')
    #instructions
    instructions = drink.get('strInstructions')
    #ingredients
    ingredients =[]
    for num in range(1,16):
        ingredient = drink.get(f'strIngredient{num}')
        measure = drink.get(f'strMeasure{num}')
        if ingredient:
            ingredients.append((ingredient,measure))

    return render_template('details_cocktail.html',cocktail_name=cocktail_name, image=image, instructions=instructions, ingredients=ingredients)

@app.route("/register", methods=['GET','POST'])
def register():
    """Create registration form for user"""
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        if(User.query.filter_by(username=username).first() is None):
            newUser = User.encrypt(username,password,first_name,last_name)
            db.session.add(newUser)
            db.session.commit()
            flash("Your User Account has been created")
            return redirect(url_for('login'))
        else:
            flash("Username already taken", 'danger')
            return render_template('register.html', form=form)
    
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    """Directs to user login page"""
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and User.authenticate(username,password):
            flash('Login successful!', 'success')
            session['user_id']= user.id
            session['username']= user.username
            return redirect(f"/{user.id}/{user.username}/profile")
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
            return redirect("/login")

    else:
        return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """Handle logout of user."""
    session.pop("username")
    flash("You has logged out!", "success")
    return redirect("/login")

@app.route('/<int:user_id>/<username>/profile')
def user_profile(user_id,username):
    """Show user profile."""
    if 'username' in session and session['username'] ==  username:
        user = User.query.get_or_404(user_id)
        return render_template('user-profile.html', user=user)
    else:
        flash('You need to log in to access this page','danger')
        return redirect('/login')

@app.route('/like', methods=["POST"])
def like_cocktail():
    """check liked cocktail to user and save to user profile."""
    if 'username' not in session:
        flash('You need to be logged in to like the cocktail','danger')
        return redirect(url_for('login'))
    
    cocktail_name = request.form.get('cocktail_name')

    user = User.query.filter_by(username=session['username']).first()
    if user is None:
        flash('User not found','danger')
        return redirect(url_for('login'))

    already_liked = LikedCocktail.query.filter_by(user_id=user.id, cocktail_name=cocktail_name).first()
    if already_liked:
        flash('This cocktail is already on your list!','warning')
        return redirect(url_for('user_profile', user_id=user.id, username=user.username))
    
    liked_cocktail = LikedCocktail(user_id=user.id, cocktail_name=cocktail_name)
    db.session.add(liked_cocktail)
    db.session.commit()

    flash('Cocktail saved to your profile!','success')
    return redirect(url_for('user_profile', user_id = user.id, username=user.username))

@app.route('/remove_like/<cocktail_name>', methods=["POST"])
def remove_like(cocktail_name):
    if 'username' not in session:
        flash('You need to be logged in to remove the cocktail','danger')
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=session['username']).first()
    if user is None:
        flash('User is not found','danger')
        return redirect(url_for('login'))
    
    cocktail = LikedCocktail.query.filter_by(user_id=user.id, cocktail_name=cocktail_name).first()
    if cocktail:
        db.session.delete(cocktail)
        db.session.commit()
    
    return redirect(url_for('user_profile', user_id=user.id, username=user.username))

              





   

    
    