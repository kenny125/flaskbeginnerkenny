from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('template/home.html')


@app.route('/about')
def about():
    return '<h3>About Page</h3>'


if __name__ == '__main__':
    app.run(debug=True)
