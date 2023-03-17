from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():


    return



if __name__ == '__main__':
    app.run(debug=True)


