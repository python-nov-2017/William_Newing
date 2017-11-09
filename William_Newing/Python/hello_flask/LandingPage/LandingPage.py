from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_coding_dojo():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas_page():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def new_dojo():
    return render_template('dojos.html')

app.run(debug=True)
