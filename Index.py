from datetime import datetime
import os
import pandas as pd

class Documento:
    def __init__(self, cod_art, descrizione_art, data_doc = datetime.now() ):
        self.setCodice(cod_art)
        self.setDescrizione(descrizione_art)
        self.data_doc  = data_doc

    def setCodice(self, cod_art):
        self.__cod_art = cod_art
        return f"Inserito il codice: {self.__cod_art}"

    def setDescrizione(self, descrizione_art):
        self.__descrizione_art = descrizione_art
        return f"Inserito il codice: {self.__descrizione_art}"
    
    def data(self):
        data_doc = datetime.now()

    def registro():
        data = pd.read_csv('registrazioni.csv')
        return data

    def __str__(self):
        lista=os.listdir()
        if 'registrazioni.csv' not in lista:
            with open('registrazioni.csv','w') as x:
                x.write("codiceArticolo,DescrizioneArticolo,DataRegistrazione\n")
                x.write(f"{self.__cod_Art},{self.__descrizione_art},{self.data_doc}\n")
        else:
            with open('registrazioni.csv','a') as x:
                x.write(f"{self.__cod_art},{self.__descrizione_art},{self.data_doc}\n")
                
        return f"Articolo Inserito:\n CODICE: {self.__cod_art}\n DESCRIZIONE: {self.__descrizione_art}\n DATA: {self.data_doc}\n"
