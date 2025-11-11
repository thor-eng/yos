from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <h1>Login Page</h1>
        <form action="/login" method="post">
            <input id="username" name="username" placeholder="Enter username"><br>
            <input id="password" name="password" placeholder="Enter password" type="password"><br>
            <button id="login-btn" type="submit">Login</button>
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "1234":
        return "<h2>Login successful ✅</h2>"
    else:
        return "<h2>Login failed ❌</h2>"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
