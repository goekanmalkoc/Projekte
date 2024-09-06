from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey123'  # Gizli anahtar oturumları güvenli hale getirmek için
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # Veritabanı için SQLite kullanıyoruz
db = SQLAlchemy(app)

# Kullanıcı tablosu modeli
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Yapılacaklar listesi tablosu modeli
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Ana sayfa - Giriş sayfası
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user_id'] = user.id
            return redirect(url_for('todo_list'))
        else:
            return "Yanlış kullanıcı adı veya şifre!"
    
    return render_template('login.html')

# Kayıt sayfası
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Yeni kullanıcı ekleme
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('register.html')

# Kullanıcının to-do listesi
@app.route('/todo', methods=['GET', 'POST'])
def todo_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    todos = Todo.query.filter_by(user_id=user_id).all()

    if request.method == 'POST':
        task = request.form['task']
        new_task = Todo(task=task, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('todo_list'))

    return render_template('todo.html', todos=todos)

# Kullanıcının çıkış yapması
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Veritabanı tablolarını oluşturur
    app.run(debug=True, port=4000)

