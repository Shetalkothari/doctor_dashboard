import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from lung_model import predict_lung_cancer
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.secret_key = 'your_secret_key'  # change this to a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "error")
            return redirect(url_for('signup'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully. Please login.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Login successful", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password", "error")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please log in first", "error")
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/upload')
def upload():
    if 'user_id' not in session:
        flash("Please log in first", "error")
        return redirect(url_for('login'))
    return render_template('upload.html')

@app.route('/diabetes')
def diabetes():
    if 'user_id' not in session:
        flash("Please log in first", "error")
        return redirect(url_for('login'))
    return render_template('diabetes.html', username=session['username'])

@app.route('/lung-cancer')
def lung():
    if 'user_id' not in session:
        flash("Please log in first", "error")
        return redirect(url_for('login'))
    return render_template('lung.html', username=session['username'])

@app.route('/predict/lung-cancer', methods=['POST'])
def predict_lung():
    if 'image' not in request.files:
        flash("No file part", "error")
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        flash("No selected file", "error")
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Here you can load the image and pass it to your ML model
        # result = predict_lung_cancer(filepath)
        # result = "Sample Result: No signs of lung cancer detected."
        result = predict_lung_cancer(filepath)

        return render_template('lung_result.html', filename=filename, result=result)

    flash("Invalid file format", "error")
    return redirect(url_for('lung_cancer'))  # redirect to the lung cancer page

@app.route('/breast')
def breast():
    if 'user_id' not in session:
        flash("Please log in first", "error")
        return redirect(url_for('login'))
    return render_template('breast.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for('login'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
