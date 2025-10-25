import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Post
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus_connect.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    search_query = request.args.get('search', '')
    filter_type = request.args.get('filter', 'all')
    
    query = Post.query
    
    if search_query:
        query = query.filter(
            (Post.title.contains(search_query)) | 
            (Post.body.contains(search_query))
        )
    
    if filter_type == 'official':
        query = query.filter_by(post_type='notice', is_official=True)
    elif filter_type == 'club':
        query = query.filter_by(is_official=False)
    
    posts = query.order_by(Post.created_at.desc()).all()
    
    return render_template('index.html', posts=posts, search_query=search_query, filter_type=filter_type)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_posts = Post.query.filter_by(author_id=current_user.id).order_by(Post.created_at.desc()).all()
    return render_template('dashboard.html', posts=user_posts)

@app.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        post_type = request.form.get('post_type')
        
        event_date = request.form.get('event_date')
        event_time = request.form.get('event_time')
        event_location = request.form.get('event_location')
        
        new_post = Post(
            title=title,
            body=body,
            post_type=post_type,
            author_id=current_user.id,
            is_official=current_user.role == 'admin',
            event_date=datetime.strptime(event_date, '%Y-%m-%d').date() if event_date else None,
            event_time=event_time if event_time else None,
            event_location=event_location if event_location else None
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_post.html')

@app.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if post.author_id != current_user.id:
        flash('You can only delete your own posts', 'error')
        return redirect(url_for('dashboard'))
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous')
        category = request.form.get('category')
        message = request.form.get('message')
        
        flash('Thank you for your feedback! It has been sent to the admin team.', 'success')
        return redirect(url_for('index'))
    
    return render_template('feedback.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        organization = request.form.get('organization')
        role = request.form.get('role', 'club')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            full_name=full_name,
            organization=organization,
            role=role
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

def init_db():
    with app.app_context():
        db.create_all()
        
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                password_hash=generate_password_hash('admin123'),
                full_name='Campus Admin',
                organization='Administration',
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print('Admin user created: username=admin, password=admin123')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
