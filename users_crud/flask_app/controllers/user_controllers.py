from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user_model import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template('home.html', all_users = users)

@app.route('/create_user', methods=['post'])
def create_user():
    print(request.form)
    user = User.save(request.form)
    return redirect('/users')

@app.route('/new_user')
def new_user():
    return render_template('create.html')

@app.route('/show_user/<int:id>')
def show_user(id):
    data = {
        'id' : id
    }
    return render_template('show.html', one_user = User.get_one_user(data))

@app.route('/home')
def home():
    return redirect('/users')

@app.route('/edit_user/<int:id>')
def edit_user(id):
    data =  {
        'id' :id
    }
    return render_template('edit_user.html', one_user = User.get_one_user(data))

@app.route('/update_user/<int:id>', methods = ['post'])
def update_user(id):
    print(request.form)
    User.update_user(request.form, id)
    return redirect('/users')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete_user(id)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)