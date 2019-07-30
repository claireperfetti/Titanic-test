import pandas as pd
from sqlalchemy import create_engine
import os

df = pd.read_csv('data/train.csv')
 #url = 'postgres://claire:user@localhost:5432/titanic'
url= 'postgres://owabbuyinrwxmr:ef726cd8b809b8f61f25069ed11714e1abec0e48835fe04939701e9ae27a8ec8@ec2-54-217-206-65.eu-west-1.compute.amazonaws.com:5432/dm8g38467oti0'
#url = 'postgres://etcigfzo:7qGx3WmRjo5AnJnvsBQbv7OzuyFt_PVD@manny.db.elephantsql.com:5432/etcigfzo'
engine = create_engine(url)
df.to_sql('passengers', con=engine)

df = pd.read_csv('data/test.csv')
# #url = 'postgres://claire:user@localhost:5432/titanic'
# url = 'postgres://etcigfzo:7qGx3WmRjo5AnJnvsBQbv7OzuyFt_PVD@manny.db.elephantsql.com:5432/etcigfzo'
engine = create_engine(url)
df.to_sql('test_passengers', con=engine)