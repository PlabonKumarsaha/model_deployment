from flask import Flask
from flask import request
from flask_cors import CORS
import sklearn
import joblib

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return '<h1>API server is working</h1>'


@app.route('/predict', methods=['GET'])
def home():
    model =joblib.load('res/marriage_age_predict_model.ml')
    age_predict = model.predict([[request.args['gender'],
                                  request.args['religion'],
                                  request.args['caste'],
                                  request.args['mother_tongue'],
                                  request.args['country'],
                                  request.args['height_cms']]])
    print("value", age_predict)
    return str(age_predict)

    # if __name__ == '__main__':
    app.run()
