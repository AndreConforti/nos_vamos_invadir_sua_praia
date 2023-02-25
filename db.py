import sqlite3
import os

class DBManager():
    def __init__(self) -> None:
        try:
            os.mkdir('database')
        except:
            pass
        self.con = sqlite3.connect('database/agenda.db')
        self._create_tables()
        self.cur = self.con.cursor()

    def add_data(self, table, data):
        query = f"""INSERT INTO {table} VALUES(?, ?, ?, ?, ?)"""
        try:
            self.cur.execute(query, data)
            self.con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_data(self, table, column, value):
        self.cur.execute(f"SELECT * FROM {table} WHERE {column}='{value}'")
        result = self.cur.fetchall()
        return result

    def get_all(self, table):
        self.cur.execute(f"SELECT * FROM {table}")
        result = self.cur.fetchall()
        return result

    def remove_data(self, table, data):
        column, value = data
        try:
            self.cur.execute(f"DELETE FROM {table} WHERE {column}={value}")
            self.con.commit()
            return True
        except Exception as e:get_data(self, table, column, value)
            print(e)
            return False

    def _create_tables(self):
        cur = self.con.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS clientes (
                nome CHAR,
                cpf CHAR,
                telefone CHAR,
                email CHAR,
                saldo REAL)
            """
        cur.execute(query)
        query = """
            CREATE TABLE IF NOT EXISTS reservas (
                cliente CHAR,
                quadra INTEGER,
                data DATE,
                hora_inicio CHAR,
                hora_fim CHAR)
            """
        cur.execute(query)
        self.con.commit()
