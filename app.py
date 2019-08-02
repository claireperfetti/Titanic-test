from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import pandas as pd
import numpy as np
from ml_model.run_pipeline import train_model
from ml_model.prediction import make_prediction
from sqlalchemy import create_engine

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.environ['DATABASE_URL']
# Database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
#url = 'postgres://vmwjdsxv:7rW8rmQet0580-Uqai2gAdojctbt9Bkw@raja.db.elephantsql.com:5432/vmwjdsxv'
engine = create_engine(DATABASE_URL)

# make a predict
@app.route('/predict', methods=['POST'])
def predict():
    y_test = make_prediction(input_data=request.get_json())
    #df = pd.DataFrame(request.get_json(), index=[0])
    df = pd.DataFrame(request.get_json())
    df['Survived'] = y_test
    df.to_sql('predictions', con=engine,if_exists='append')
    return jsonify((y_test.tolist()))

@app.route('/data', methods=['GET'])
def data():
    return pd.read_sql('passengers', DATABASE_URL).to_dict()

@app.route('/test', methods=['GET'])
def data_test():
    test_dic=pd.read_sql('test_passengers', con=engine).head(5)
    test_dic=test_dic.to_json(orient='records')
    return test_dic
# 
#make prediction from whole database
@app.route('/predict_db', methods=['POST'])
def predict_all():
    db_test=pd.read_sql('test_passengers', con=engine,index_col='index')
    y_test = make_prediction(db_test)
    db_test['Survived'] = y_test
    test_dic=db_test.to_dict(orient='index')
    db_test.to_sql('prediction_testdb',con=engine,if_exists='append',index=False)
    return jsonify(test_dic)

@app.route('/train', methods=['GET'])
def train():
    train_model()
    return "Training completed"


# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
    #app.run(debug=True)
