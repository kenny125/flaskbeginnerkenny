from flask import Flask, render_template

app = Flask(__name__)
# added comments
# added more comments

@app.route('/')
@app.route('/home')
def home():
    return '<h2>Home Page</h2>'


@app.route('/about')
def about():
    return '<h3>About Page</h3>'


if __name__ == '__main__':
    app.run(debug=True)
