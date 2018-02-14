import os
import sys

import flask
from flask import request, render_template, redirect, url_for

app = flask.Flask(__name__)

from User import persist_user
# import User



@app.route('/')
def home():
    return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            op = persist_user(data)
            # print('request params: ', data)
            print('op', op)
            message = 'Registered!'

    except Exception as e:
        render_template('register.html', error=e.message)  # GET or invalid cred

    return render_template('register.html', message=message)



# if __name__ == '__main__':
#     sys.path.append(os.path.dirname(__name__))
#     User.createDB()
#     app.run(debug=True)
