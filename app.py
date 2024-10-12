from flask import Flask, render_template_string, request, redirect, flash, url_for, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in users and bcrypt.check_password_hash(users[email], password):
            session['user'] = email 
            flash('Login successful!', 'success')
            return redirect(url_for(''))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))

    return render_template_string(open('index.html').read())
if __name__ == '__main__':
    app.run(debug=True, port=5000)