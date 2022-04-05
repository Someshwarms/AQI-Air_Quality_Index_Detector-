from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('AQI_new_model5.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/index1')
def index1():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    pm25 = float(request.form.get('pm25'))
    pm10 = float(request.form.get('pm10'))
    no = float(request.form.get('no'))
    no2 = float(request.form.get('no2'))
    nh3 = float(request.form.get('nh3'))
    co = float(request.form.get('co'))
    so2 = float(request.form.get('so2'))
    o3 = float(request.form.get('o3'))
    Ben = float(request.form.get('Ben'))
    xy = float(request.form.get('xy'))
    tou = float(request.form.get('tou'))


    result = model.predict(np.array([pm25,pm10,no,no2,nh3,co,so2,o3,Ben,xy,tou]).reshape(1,11))


    return render_template('result.html',result=result)


if __name__ == '__main__':
    app.run(debug=True)