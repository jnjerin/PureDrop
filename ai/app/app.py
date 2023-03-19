from flask import Flask, render_template, request
from flask_cors import CORS
from pycaret.classification import *
from sklearn import *

import pandas
import pickle


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins":"*"
    }
})
ai_model = 'ai/ai-models/wpp_model_dev_'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    # loaded_model = pickle.load(open(ai_model, 'rb'))
    #new = [[7, 215, 12000, 7, 334, 415, 16, 80, 3]]
    # results = loaded_model.predict(new)

    '''
        Load model
    '''
    loaded_model = load_model(ai_model)

    '''
        Fetch payload
    '''
    ph = request.json['ph']
    hardness = request.json['hardness']
    solids = request.json['solids']
    chloramines = request.json['chloramines']
    sulphate = request.json['sulphate']
    conductivity = request.json['conductivity']
    organic_carbon = request.json['organic_carbon']
    trihalomethanes = request.json['trihalomethanes']
    turbidity = request.json['turidity']

    new = [[ph, hardness, solids, chloramines, sulphate, conductivity, organic_carbon, trihalomethanes, turbidity]]
    
    #Predict payload
    results = predict_model(loaded_model, data=new)

    return results
print(pycaret.__version__)

if __name__ == '__main__':
    app.run(debug=True)


