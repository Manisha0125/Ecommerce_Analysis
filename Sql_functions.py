# importing dependencies

import os

import mysql.connector
from dotenv import load_dotenv
import pandas as pd

# loading credentials

load_dotenv()

user = os.getenv('USER')
password = os. getenv('PASSWORD')
host = os.getenv('HOST')
database= 'swiftmarket'

# establishing connection

connection = mysql.connector.connect(user=user,
                                     password=password,
                                     host=host,
                                     database=database)

cursor = connection.cursor()

# to read sql query

def read_query(query):
   """ Reading sql queries.Only for select queries.
       Returns: pd.DataFrame"""

   cursor.execute(query)
   rows = cursor.fetchall()
   return pd.DataFrame(data=rows, columns=cursor.column_names) 

 
if __name__=='__main__':
       query = 'show tables;'
       print(query)
       df = read_query(query=query)
       print(df)





