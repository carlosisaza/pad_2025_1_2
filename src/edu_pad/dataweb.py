import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime




class DataWeb:
    def __init__(self):
        self.url = "https://es.finance.yahoo.com/quote/GC%3DF/history/"
    

    def obtener_datos(self):
        try:
            # url , cabeceras
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            respuesta = requests.get(self.url,headers=headers)
            if respuesta.status_code != 200:
                print("La url saco error, no respondio o no existe")
            #print(respuesta.text)
            soup = BeautifulSoup(respuesta.text,'html.parser')
            tabla = soup.select_one('div[data-testid="history-table"] table')
            nombre_columnas = [th.get_text(strip=True) for th in tabla.thead.find_all('th')]
            
            filas = []
            for tr in tabla.tbody.find_all('tr'):
                columnas = [ td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columnas) == len(nombre_columnas):
                    filas.append(columnas)
            df = pd.DataFrame(filas,columns=nombre_columnas).rename(columns = {
                'Fecha': 'fecha',
                'Abrir': 'abrir',
                'Máx.': 'max',
                'Mín.': 'min',
                'CerrarPrecio de cierre ajustado para splits.': 'cerrar',
                'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.': 'cierre_ajustado',
                'Volumen':'volumen'
            })

            #df.to_excel("dataweb.xlsx")
            #print(nombre_columnas)
            #print(filas)
 


            return df
        except Exception as err:
            print("Error en la funcion obtener_datos")
            df = pd.DataFrame()
   
    
#dw = DataWeb()
#dw.obtener_datos()
#print(dw.url)