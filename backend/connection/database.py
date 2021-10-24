import sqlite3
from sqlite3 import Error


def connect():
    try:
        connection = sqlite3.connect(
            "/home/lucas/Documents/UNIVESP-PI/2021/SBP-sus/db/banco_de_dados.db")
    except Error:
        print(Error)

    return connection
