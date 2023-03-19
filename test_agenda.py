# import datetime
# import csv

# from classes.agenda import Agenda
# from classes.quadra import Quadra_BeachTenis
# from classes.cliente import Cliente
# from classes.reserva import Reserva


# def test_save_agenda():
#     # Crie uma instância de Agenda com algumas reservas
#     agenda = Agenda()
#     agenda.reservas = [Reserva(cliente=Cliente(nome="Fulano", cpf="12345678900", telefone="55555555", email="fulano@test.com"),            quadra=Quadra_BeachTenis(nome_quadra="Quadra 1", min_players=2, max_players=4, drenagem=True),            data="2023-04-01",            hora_inicio=10,            duracao=2        ),        Reserva(            cliente=Cliente(nome="Ciclano", cpf="98765432100", telefone="55555555", email="ciclano@test.com"),            quadra=Quadra_BeachTenis(nome_quadra="Quadra 2", min_players=2, max_players=4, drenagem=True),            data="2023-04-01",            hora_inicio=14,            duracao=1        )    ]

#     # Salva as reservas em um arquivo CSV temporário
#     filename = "test_agenda.csv"
#     agenda.save_agenda(filename)

#     # Abre o arquivo CSV temporário e verifica se as informações foram salvas corretamente
#     with open(filename, "r", newline="") as csvfile:
#         reader = csv.DictReader(csvfile)
#         rows = [row for row in reader]

#     assert len(rows) == 2
#     assert rows[0]["nome"] == "Fulano"
#     assert rows[0]["cpf"] == "12345678900"
#     assert rows[0]["telefone"] == "55555555"
#     assert rows[0]["email"] == "fulano@test.com"
#     assert rows[0]["nome_quadra"] == "Quadra 1"
#     assert rows[0]["min_players"] == "2"
#     assert rows[0]["max_players"] == "4"
#     assert rows[0]["data"] == "2023-04-01"
#     assert rows[0]["hora_inicio"] == "10"
#     assert rows[0]["duracao"] == "2"

#     assert rows[1]["nome"] == "Ciclano"
#     assert rows[1]["cpf"] == "98765432100"
#     assert rows[1]["telefone"] == "55555555"
#     assert rows[1]["email"] == "ciclano@test.com"
#     assert rows[1]["nome_quadra"] == "Quadra 2"
#     assert rows[1]["min_players"] == "2"
#     assert rows[1]["max_players"] == "4"
#     assert rows[1]["data"] == "2023-04-01"
#     assert rows[1]["hora_inicio"] == "14"
#     assert rows[1]["duracao"] == "1"