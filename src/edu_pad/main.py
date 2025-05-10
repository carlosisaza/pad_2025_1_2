from dataweb import DataWeb
import pandas as pd



def main():
    dataweb = DataWeb()
    df = dataweb.obtener_datos()
    df.to_csv("data_web.csv")



if __name__ == "__main__":
    main()