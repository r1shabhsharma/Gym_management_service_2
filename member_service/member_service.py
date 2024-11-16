# member_service.py
from flask import Flask, request, jsonify
from models import db, Membership

# Initialize the Flask app
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize the database with the app
db.init_app(app)

# Route to display a welcome message
@app.route('/')
def home():
    return "Welcome to the Gym Management System!"

# Route to add a new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(
        name=data['name'], gender=data['gender'], age=data['age'],
        mobile=data['mobile'], weight=data['weight'],
        height=data['height'], join_date=data['join_date'],
        expiry_date=data['expiry_date']
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member added successfully'}), 201

# Route to get all members
@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([member.to_dict() for member in members])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
