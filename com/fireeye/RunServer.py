
import sys, os
sys.path.append(os.path.dirname(__name__))
import flask

from app import app
import User


if __name__ == '__main__':
    User.createDB()
    app.run(debug=True)
