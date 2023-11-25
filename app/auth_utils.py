from app import app, db
from app.models import Role, UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity

def init_roles():
    with app.app_context():
        admin_role = Role.query.filter_by(name='admin').first()

    if not admin_role:
        admin_role = Role(name="admin")
        user_role = Role(name="user")

        db.session.add(admin_role)
        db.session.add(user_role)

        db.session.commit()

@app.route('/protected')
@jwt_required()
def protected():
    current_user_username = get_jwt_identity()
    current_user = UserModel.query.filter_by(username=current_user_username).first()

    if current_user.role.name == 'admin':
        return {'message': 'You have access to this protected resource as an admin'}
    else:
        return {'message': 'You have access to this protected resource as a regular user'}
