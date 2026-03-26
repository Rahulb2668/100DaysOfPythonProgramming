from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from User import User
from Todo import Todo
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'some-super-secret-string'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
@login_required
def get_all_todo():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    if request.method == "POST":
        try: 
            content = request.form.get("content")
            new_todo = Todo(content=content, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for('get_all_todo'))
        except Exception as e:
            print(e)
    return render_template("index.html", todos=todos)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()
            if user:
                return "User already exists"

            hash_and_salt_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            new_user = User(name=name, email= email, password=hash_and_salt_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_todo'))
        except Exception as e:
            print(e)

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try: 
            email = request.form.get("email") 
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()
            if not user:
                return "User not found"
            
            if not check_password_hash(user.password, password):
                return "Invalid password"
            
            login_user(user)
            return redirect(url_for('get_all_todo'))
        except Exception as e:
            print(e)
    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return render_template("index.html")

@app.route("/delete/<int:todoid>", methods=["POST"])
@login_required
def delete_todo(todoid):
    todo = Todo.query.get(todoid)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('get_all_todo'))

@app.route("/update/<int:todoid>", methods=["GET","POST"])
@login_required
def update_todo(todoid):
    todo = Todo.query.get(todoid)
    if request.method == "POST":
        try: 
            todo.content = request.form.get("content")
            db.session.commit()
            return redirect(url_for('get_all_todo'))
        except Exception as e:
            print(e)
    return render_template("update.html", todo=todo)
if __name__ == "__main__":
    app.run(debug=True)