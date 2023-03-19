import pytest

from datetime import date, timedelta

from classes.reserva import Reserva
from classes.cliente import Cliente
from classes.quadra import Quadra_BeachTenis


@pytest.fixture
def reserva():
    cliente = Cliente(nome='Andre Conforti', cpf='27875969832', telefone='988779988', email='andreconforti@gmail.com')
    quadra = Quadra_BeachTenis(nome_quadra='Quadra 1', min_players=2, max_players=4)
    data = date.today()
    hora_inicio = '10'
    duracao = 1
    return Reserva(cliente=cliente, quadra=quadra, hora_inicio=hora_inicio, duracao=duracao, data=data)


def test_valor_reserva(reserva):
    """Verifica se o valor está correto para uma reserva de uma hora ou três horas"""
    assert reserva.valor_reserva() == 100
    reserva.duracao = 3
    assert reserva.valor_reserva() == 250


def test_hora_inicio_valida(reserva):
    """Apresenta uma exceção caso tente colocar um horário inválido"""
    reserva.hora_inicio = 8
    with pytest.raises(ValueError):
        reserva.data = date.today()


def test_data_valida(reserva):
    """Verifica se uma data futura é considerada válida."""
    reserva.data = date.today() + timedelta(days=1)
    assert reserva.data == date.today() + timedelta(days=1)


def test_altera_data_reserva(reserva):
    """Verifica se a data pode ser alterada corretamente e se a nova data também está correta"""
    data_nova = date(2023, 4, 18)
    reserva.data = data_nova
    assert reserva.data == data_nova

