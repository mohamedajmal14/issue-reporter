from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your email'
app.config['MAIL_PASSWORD'] = 'your password'

mail = Mail(app)

app.secret_key = 'your_secret_key'  # Replace with a secure secret key

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

# In-memory dictionary for storing user credentials (replace with a database)
users = {
    'user1': {'password': 'password1', 'email': 'user1@gmail.com'},
    'user2': {'password': 'password2', 'email': 'user2@gmail.com'}
}

# In-memory dictionary for storing password reset tokens and associated emails
reset_tokens = {}

@app.route('/')
def home():
    return render_template('exc.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username]['password'] == password:
        session.clear()
        session['logged_in'] = True
        session['username'] = username
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Login failed. Please check your username and password.', 'danger')
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        flash('You must be logged in to access the dashboard.', 'warning')
        return redirect(url_for('home'))

    return render_template('dashboard.html', username=session['username'])


@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/water_issues')
def water_issues():
    return render_template('page1.html')

@app.route('/electricity_issues')
def electricity_issues():
    return render_template('page2.html')

@app.route('/waste_management')
def waste_management():
    return render_template('page3.html')

@app.route('/maintenance_issues')
def maintenance_issues():
    return render_template('page4.html')

@app.route('/submit_waste_management_form', methods=['POST'])
def submit_waste_management_form():
    if 'logged_in' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

    # Get form data
    problem_type = request.form.get('radio')
    problem_description = request.form.get('problem_description')
    duration = request.form.get('duration')

    # Get the uploaded file
    uploaded_file = request.files['myfile']

    # Save the uploaded file to the server
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)
    else:
        filename = None

    # Send issue email with file attachment
    try:
        sender_email = users[session['username']]['email']
        msg = Message('New Waste Management Issue Report',
                      sender=sender_email,
                      recipients=['@gmail.com'])
        msg.body = f"User: {session['username']}\nProblem Type: {problem_type}\nProblem Description: {problem_description}\nDuration: {duration}"

        if filename:
            with app.open_resource(filepath) as attachment:
                msg.attach(filename, 'image/jpeg', attachment.read())

        mail.send(msg)
        flash('Waste management issue report submitted successfully. We will address the issue soon.', 'success')
    except Exception as e:
        print(f'Error sending email: {str(e)}')  # Add this line for debugging
        flash(f'Error submitting waste management issue report: {str(e)}', 'danger')

    return redirect(url_for('home'))

@app.route('/submit_water_issues_form', methods=['POST'])
def submit_water_issues_form():
    if 'logged_in' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

    # Get form data
    problem_type = request.form.get('radio')
    problem_description = request.form.get('problem_description')
    duration = request.form.get('duration')

    # Get the uploaded file
    uploaded_file = request.files['myfile']

    # Save the uploaded file to the server
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)
    else:
        filename = None

    # Send issue email with file attachment
    try:
        sender_email = users[session['username']]['email']
        msg = Message('New Water Issue Report',
                      sender=sender_email,
                      recipients=['@gmail.com'])
        msg.body = f"User: {session['username']}\nProblem Type: {problem_type}\nProblem Description: {problem_description}\nDuration: {duration}"

        if filename:
            with app.open_resource(filepath) as attachment:
                msg.attach(filename, 'image/jpeg', attachment.read())

        mail.send(msg)
        flash('Water issue report submitted successfully. We will address the issue soon.', 'success')
    except Exception as e:
        print(f'Error sending email: {str(e)}')  # Add this line for debugging
        flash(f'Error submitting water issue report: {str(e)}', 'danger')

    return redirect(url_for('home'))

@app.route('/submit_electricity_issues_form', methods=['POST'])
def submit_electricity_issues_form():
    if 'logged_in' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

    # Get form data
    problem_type = request.form.get('radio')
    problem_description = request.form.get('problem_description')
    duration = request.form.get('duration')

    # Get the uploaded file
    uploaded_file = request.files['myfile']

    # Save the uploaded file to the server
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)
    else:
        filename = None

    # Send issue email with file attachment
    try:
        sender_email = users[session['username']]['email']
        msg = Message('New Electricity Issue Report',
                      sender=sender_email,
                      recipients=['@gmail.com'])
        msg.body = f"User: {session['username']}\nProblem Type: {problem_type}\nProblem Description: {problem_description}\nDuration: {duration}"

        if filename:
            with app.open_resource(filepath) as attachment:
                msg.attach(filename, 'image/jpeg', attachment.read())

        mail.send(msg)
        flash('Electricity issue report submitted successfully. We will address the issue soon.', 'success')
    except Exception as e:
        print(f'Error sending email: {str(e)}')  # Add this line for debugging
        flash(f'Error submitting electricity issue report: {str(e)}', 'danger')

    return redirect(url_for('home'))

@app.route('/submit_maintenance_issues_form', methods=['POST'])
def submit_maintenance_issues_form():
    if 'logged_in' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

    # Get form data
    problem_type = request.form.get('radio')
    problem_description = request.form.get('problem_description')
    duration = request.form.get('duration')

    # Get the uploaded file
    uploaded_file = request.files['myfile']

    # Save the uploaded file to the server
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)
    else:
        filename = None

    # Send issue email with file attachment
    try:
        sender_email = users[session['username']]['email']
        msg = Message('New maintenance Issue Report',
                      sender=sender_email,
                      recipients=['@gmail.com'])
        msg.body = f"User: {session['username']}\nProblem Type: {problem_type}\nProblem Description: {problem_description}\nDuration: {duration}"

        if filename:
            with app.open_resource(filepath) as attachment:
                msg.attach(filename, 'image/jpeg', attachment.read())

        mail.send(msg)
        flash('Maintenance issue report submitted successfully. We will address the issue soon.', 'success')
    except Exception as e:
        print(f'Error sending email: {str(e)}')  # Add this line for debugging
        flash(f'Error submitting water issue report: {str(e)}', 'danger')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
