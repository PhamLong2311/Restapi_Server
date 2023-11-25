from app import app, db
from app.auth_utils import init_roles, protected

def run(host='127.0.0.1',post=5000):
       with app.app_context():
        db.create_all()
        init_roles()

       app.run(debug=True)
if __name__ == '__main__':
    run(host='127.0.0.1',post=5000)
