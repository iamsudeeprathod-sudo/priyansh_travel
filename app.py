from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travels.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

# Models
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    travelers = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def index():
    destinations = [
        {'name': 'Maldives', 'price': '$299', 'img': 'destinations/maldives.jpg'},
        {'name': 'Bali', 'price': '$249', 'img': 'destinations/bali.jpg'},
        {'name': 'Paris', 'price': '$399', 'img': 'destinations/paris.jpg'},
        {'name': 'Dubai', 'price': '$349', 'img': 'destinations/dubai.jpg'},
        {'name': 'Goa', 'price': '$199', 'img': 'destinations/goa.jpg'},
        {'name': 'Switzerland', 'price': '$499', 'img': 'destinations/switzerland.jpg'}
    ]
    return render_template('index.html', destinations=destinations)

@app.route('/destinations')
def destinations():
    destinations = [
        {'name': 'Maldives', 'category': 'beach', 'price': '$299', 'img': 'destinations/maldives.jpg', 'rating': 4.9, 'duration': '7 Days', 'reviews': 1247},
        {'name': 'Bali', 'category': 'beach', 'price': '$249', 'img': 'destinations/bali.jpg', 'rating': 4.8, 'duration': '6 Days', 'reviews': 987},
        {'name': 'Paris', 'category': 'culture', 'price': '$399', 'img': 'destinations/paris.jpg', 'rating': 4.9, 'duration': '5 Days', 'reviews': 1562},
        {'name': 'Dubai', 'category': 'luxury', 'price': '$349', 'img': 'destinations/dubai.jpg', 'rating': 4.7, 'duration': '4 Days', 'reviews': 892},
        {'name': 'Goa', 'category': 'beach', 'price': '$199', 'img': 'destinations/goa.jpg', 'rating': 4.6, 'duration': '5 Days', 'reviews': 2345},
        {'name': 'Switzerland', 'category': 'adventure', 'price': '$499', 'img': 'destinations/switzerland.jpg', 'rating': 4.9, 'duration': '8 Days', 'reviews': 673},
        {'name': 'Thailand', 'category': 'beach', 'price': '$279', 'img': 'destinations/thailand.jpg', 'rating': 4.8, 'duration': '7 Days', 'reviews': 1456},
        {'name': 'New York', 'category': 'culture', 'price': '$429', 'img': 'destinations/newyork.jpg', 'rating': 4.7, 'duration': '6 Days', 'reviews': 789},
        {'name': 'Mauritius', 'category': 'luxury', 'price': '$389', 'img': 'destinations/mauritius.jpg', 'rating': 4.9, 'duration': '7 Days', 'reviews': 456},
        {'name': 'Himachal', 'category': 'adventure', 'price': '$229', 'img': 'destinations/himachal.jpg', 'rating': 4.8, 'duration': '6 Days', 'reviews': 1234},
        {'name': 'Singapore', 'category': 'luxury', 'price': '$359', 'img': 'destinations/singapore.jpg', 'rating': 4.7, 'duration': '5 Days', 'reviews': 987},
        {'name': 'Kerala', 'category': 'culture', 'price': '$189', 'img': 'destinations/kerala.jpg', 'rating': 4.6, 'duration': '5 Days', 'reviews': 2100}
    ]
    return render_template('destinations.html', destinations=destinations)

@app.route('/packages')
def packages():
    return render_template('packages.html')

@app.route('/test')
def test():
    return render_template('destinations.html', destinations=[
        {'name': 'Test Maldives', 'category': 'beach', 'price': '$299', 'img': 'hero-bg.jpg', 'rating': 4.9}
    ])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form
        pass
    return render_template('contact.html')

@app.route("/destinations")
def destinations_page():
    destinations = [
        {"name": "Maldives", "category": "beach", "price": "$299", "img": "destinations/maldives.jpg"},
        {"name": "Bali", "category": "beach", "price": "$249", "img": "destinations/bali.jpg"}
    ]
    return render_template("destinations.html", destinations=destinations)

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    booking = Booking(
        name=data['name'],
        email=data['email'],
        destination=data['destination'],
        travelers=data['travelers']
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Booking confirmed!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)

@app.route('/destinations')
def destinations():
    destinations = [
        {'name': 'Maldives', 'category': 'beach', 'price': '$299', 'img': 'destinations/maldives.jpg', 'rating': 4.9},
        {'name': 'Bali', 'category': 'beach', 'price': '$249', 'img': 'destinations/bali.jpg', 'rating': 4.8},
        {'name': 'Paris', 'category': 'culture', 'price': '$399', 'img': 'destinations/paris.jpg', 'rating': 4.9},
        # Add more...
    ]
    return render_template('destinations.html', destinations=destinations)