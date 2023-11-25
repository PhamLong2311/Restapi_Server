from app import db

#Thay đổi mô hình người dùng
class Role(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),unique=True,nullable=False)



class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
# def create_tables():
db.create_all()
