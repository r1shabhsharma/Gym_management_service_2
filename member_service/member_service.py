from flask import Flask, request, jsonify
from models import db, Member

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the Gym Member Management System!"

# To add a new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(
        id=data['id'],
        name=data['name'],
        mobile=data['mobile'], 
        membership_Id = data['membership_Id']
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member added successfully','membership_id':new_member.id}), 201

# To get all members
@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([member.to_dict() for member in members])

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    # Retrieve the first matching record
    member = Member.query.filter_by(id=id).first()
    if member:
        return jsonify(member.to_dict())
    return jsonify({"message": "Member not found"}), 404


# Route to delete a member
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get(id)
    if member:
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Member deleted successfully','membershipId':member.membership_Id})
    return jsonify({'message': 'Member not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
