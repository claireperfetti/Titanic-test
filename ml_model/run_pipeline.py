import pandas as pd
import os
from .pipeline_preparation import prediction_pipepline
from sklearn.model_selection import train_test_split
import pickle
from sqlalchemy import create_engine

print("real", os.path.realpath(__file__))

#TRAINING_DATA_FILE = 'postgres://claire:user@localhost:5432/titanic'
TRAINING_DATA_FILE = 'postgres://etcigfzo:7qGx3WmRjo5AnJnvsBQbv7OzuyFt_PVD@manny.db.elephantsql.com:5432/etcigfzo'

#TESTING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/datasets/test.csv'
MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/saved_model/model.sav'
engine = create_engine(TRAINING_DATA_FILE)


def _save_model(model):
    pickle.dump(model, open(MODEL_PATH, 'wb'))


def train_model():
    data = pd.read_sql('passengers', con=engine)
    data.dropna(subset=['Survived'], inplace=True)
    X = data.drop('Survived', axis=1)
    y = data['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
    prediction_pipepline.fit(X_train, y_train)
    _save_model(prediction_pipepline)
    return prediction_pipepline.score(X_test, y_test)

if __name__ == '__main__':
    print(train_model())
