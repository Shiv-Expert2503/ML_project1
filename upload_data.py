from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://<User_Name>:<Password>@cluster0.yc3hy9y.mongodb.net/?retryWrites=true&w=majority"

DataBase_Name='Name'
Collection_name='Wafer_faults'

# Create a new client and connect to the server
client = MongoClient(uri)

#read data as csv
df=pd.read_csv(r'C:\Users\Dell\Desktop\PROJECT\Wafer_fault\Notebook\wafer_23012020_041211.csv')
df=df.drop('Unnamed: 0',axis=1)

#converting dataframe to json so that we can load it in mongoDB
json_records=list(json.loads(df.T.to_json()).values())


#Dumping the data into the database
client[DataBase_Name][Collection_name].insert_many(json_records)
