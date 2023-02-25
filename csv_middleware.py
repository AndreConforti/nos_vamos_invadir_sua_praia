from db import DBManager
import csv

def clientes_to_db():
    db = DBManager()
    with open('clientes.csv', 'r') as f:
        data_csv = list(csv.reader(f))
    for row in data_csv:
        db.add_data('clientes', row)

def reservas_to_db():
    db = DBManager()
    with open('reservas.csv', 'r') as f:
        data_csv = list(csv.reader(f))
    for row in data_csv:
        db.add_data('reservas', row)

def save_csv():
    clientes_to_db()
    reservas_to_db()

save_csv()