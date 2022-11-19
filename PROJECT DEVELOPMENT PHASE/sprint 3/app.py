from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list)
    loaded_model = pickle.load(open("Car Resale Value Prediction.pkl", "rb"))
    result = loaded_model.predict([to_predict])
    return result[0]


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/login', methods =['POST'])
def login():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        return render_template("index.html",y = "The Value of the Car is :   " + str(result) )

@app.route('/admin')
def admin():
    return "Hey Admin How are you?"

if __name__ == '__main__' :
    app.run(debug= True)
    
    