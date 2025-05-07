import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime




class DataWeb:
    def __init__(self):
        self.url= "https://finance.yahoo.com/quote/GC%3DF/history/"

    def obtener_datos(self):
        try:
            #url cabeceras
            headers = {
            'User-Agent': 'Mozilla/5.0'
            }
            respuesta = requests.get(self.url,headers=headers)
            if respuesta.status_code !=200:
                print("La url saco error, no respondio o no existe")
            



        except Exception as err:
            print("Error en la funcion obtener_datos")


 

    
dw = DataWeb()
print(dw.url)