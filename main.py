from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guitars')
def guitars():
    return render_template('guitars.html')

@app.route('/keyboards')
def keyboards():
    return render_template('keyboards.html')

@app.route('/drums')
def drums():
    return render_template('drums.html')

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

if __name__ == '__main__':
    app.run(debug=True)