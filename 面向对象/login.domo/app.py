from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    uname=request.args.get('uname')
    return f'主页!!!歓迎します。{uname}'

app.run(debug=True)
