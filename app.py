from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if not name or not email:
            error = 'Необходимо заполнить все поля'
        elif not name[0].isupper():
            error = 'Имя должно начинаться с большой буквы'
        else:
            resp = make_response(redirect('/welcome'))
            resp.set_cookie('name', name)
            resp.set_cookie('email', email)
            return resp
    return render_template('index.html', error=error)

@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    return render_template('welcome.html', name=name)

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    return resp

if __name__ == "__main__":
    app.run(debug=True)
