from flask import Flask, render_template

app = Flask(__name__)  
# Flask implements an application. _name_ will be the central object
#this is the GLOBAL way to instantiate Flask. Only for example

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello_barbie")
def hello_barbie():
    return render_template('index_barbie.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')    