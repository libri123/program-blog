from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_ordering.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Models for the app
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    menu_items = db.relationship('MenuItem', backref='restaurant', lazy=True)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

@app.route('/create_sample_data')
def create_sample_data():
    # Create some restaurants
    restaurant1 = Restaurant(name="Pizza Place")
    restaurant2 = Restaurant(name="Burger Joint")

    # Add some menu items
    pizza1 = MenuItem(item_name="Margherita", price=8, restaurant=restaurant1)
    pizza2 = MenuItem(item_name="Pepperoni", price=10, restaurant=restaurant1)
    burger1 = MenuItem(item_name="Cheeseburger", price=5, restaurant=restaurant2)
    burger2 = MenuItem(item_name="Veggie Burger", price=6, restaurant=restaurant2)

    # Add to the session and commit to the database
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.add(burger1)
    db.session.add(burger2)

    db.session.commit()

    return "Sample data added!"

# Create tables (schema)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.form['item']
    price = request.form['price']
    
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append({"item": item, "price": price})
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum([float(item['price']) for item in cart_items])
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

@app.route('/show_data')
def show_data():
    restaurants = db.session.execute(db.select(Restaurant)).scalars()
    return restaurants

if __name__ == '__main__':
    app.run(debug=True)