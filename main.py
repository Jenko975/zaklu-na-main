from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/motor')
def storitve():
    return render_template('motor.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/motor')
def motor():
    return render_template('motor.html')

@app.route('/turbina')
def turbina():
    return render_template('turbina.html')

@app.route('/luči')
def luči():
    return render_template('luči.html')

@app.route('/gume')
def gume():
    return render_template('gume.html')

@app.route('/platišča')
def platišča():
    return render_template('platišča.html')

if __name__ == '__main__':
    app.run(debug=True)