import pandas as pd
from sqlalchemy import create_engine
import os

url= os.environ['DATABASE_URL']
engine = create_engine(url)

df = pd.read_csv('data/train.csv')
df.to_sql('passengers', con=engine)

df = pd.read_csv('data/test.csv')
df.to_sql('test_passengers', con=engine)