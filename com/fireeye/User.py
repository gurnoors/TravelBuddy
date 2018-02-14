import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from app import app

print 'initializing constants'
USER = 'root'
PASSWORD = '123'
HOST = 'localhost'
DATABASE = 'travel_buddy'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    phone = db.Column('start_date', db.String(100))
    start_date = db.Column('end_date', db.String(100))

    def __init__(self, name, phone=None,
                 start_date=None, end_date=None):
        self.name = name
        self.phone = phone
        self.start_date = start_date
        self.end_date = end_date



def createDB():
    url = 'mysql://%s:%s@%s' % (USER, PASSWORD, HOST)
    print "URL: "+url
    engine = sqlalchemy.create_engine(url)  # connect to server
    create_str = "CREATE DATABASE IF NOT EXISTS %s ;" % (DATABASE)

    engine.execute(create_str)
    engine.execute("USE %s;" % (DATABASE))

    db.create_all()
    db.session.commit()


def validate(data):
    return True


# from kuyruk import Kuyruk
# kuyruk = Kuyruk()
# @kuyruk.task
def persist_user(data):
    if not validate(data):
        return (False, 'Bad Request')

    print("persisting user: " , data)

    user = User(name=data['name'], phone=data['phone'],
                start_date=data['start_date'], end_date=data['end_date'])
    db.session.add(user)
    db.session.commit()
    print ('user persisted: ', user)
    return (True, user)

if __name__=='__main__':
    data = {
        'name' : 'Gurnoor',
        'phone': '6692261881',
        'start_date': '02/14/2018',
        'end_date' : '02/15/2018'
    }
    print persist_user(data)