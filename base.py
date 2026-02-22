#ahora importaremos las librerias de postgres
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

conn = psycopg2.connect(host="localhost", 
                        user="postgres", 
                        database="prueba", 
                        password="oretania", 
                        port="5432", 
                        client_encoding="utf8")

query = "Select temp from dht11 limit 1"

#funcion para leer la base de datos= df = pd.read_sql(query, conn)

def OptenerTemp():
    try:
        return pd.read_sql(query, conn)
    except Exception as e:
        return 32.5
