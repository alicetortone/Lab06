from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito
import mysql.connector

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """

        cnx = get_connection()

        if cnx is None:
            return None


        cursor = cnx.cursor()
        query = 'SELECT * FROM strumento'
        cursor.execute(query)
        results = cursor.fetchall()

        strumenti = []
        for row in results:
            s = Strumento(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                bool(row[5])
            )
            strumenti.append(s)
        cursor.close()
        cnx.close()
        return strumenti

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        if not tipo or not tipo.strip():
            return []

        cnx = get_connection()

        if cnx is None:
            return None

        cursor = cnx.cursor()
        query = 'SELECT * FROM strumento WHERE tipo = %s'
        cursor.execute(query,(tipo,))
        results = cursor.fetchall()
        strumenti = []
        for row in results:
            s= Strumento(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                bool(row[5])
            )
            strumenti.append(s)
        cursor.close()
        cnx.close()
        return strumenti

