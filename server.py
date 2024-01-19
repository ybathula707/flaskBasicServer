from flask import Flask, render_template

app = Flask(__name__)  
# Flask implements an application. _name_ will be the central object

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')    