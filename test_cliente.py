import pytest
from pydantic import BaseModel, EmailStr, validator, ValidationError
# from faker import Faker

from classes.cliente import Cliente


@pytest.fixture
def lista_clientes():
    """Cria uma lista de clientes que podemos usar nos testes"""
    return [
        Cliente(nome='Andre Conforti', cpf='27875969832', telefone='19988377497', email='andre@gmail.com'),
        Cliente(nome='Alexandre Martins', cpf='22233344455', telefone='19966663333', email='alexandre@gmail.com'),
        Cliente(nome='Julay', cpf='88899977711', telefone='19911112222', email='julay@gmail.com'),
        Cliente(nome='Damaris Rocha', cpf='99900011133', telefone='19900001133', email='damaris@gmail.com'),
    ]


def test_nome_invalido(lista_clientes):
    """Após criada uma instância da classe Cliente, nome é do tipo STR e não pode ser atribuído um valor inválido. 
        Não é possível utilizar um dos itens da lista_clientes. É preciso criar uma nova instância"""
    with pytest.raises(ValidationError):
        exemplo2 = Cliente(
            nome='4l3x4ndr3 M4art1ns', 
            cpf='22233344455', 
            telefone='19966663333', 
            email='alexandre@gmail.com'
        )


def test_cpf_invalido():
    """Adiciona uma instância com CPF inválido. Se retornar uma exceção, é pq está correto."""
    with pytest.raises(ValidationError):
        exemplo3 = Cliente(
            nome='Alexandre Martins', 
            cpf='222EEE444gg', 
            telefone='19966663333', 
            email='alexandre@gmail.com'
        )


def test_telefone_invalido():
    """Instancia um objeto da classe Cliente, com telefone inválido. 
        O teste deve retornar True, pois vai acusar uma exceção."""
    with pytest.raises(ValidationError):
        exemplo4 = Cliente(
            nome='Julay', 
            cpf='22255588866', 
            telefone='1996666abc', 
            email='alexandre@gmail.com'
        )


def test_email_invalido():
    with pytest.raises(ValidationError):
        exemplo5 = Cliente(
            nome='Alexandre Martins', 
            cpf='22255588866', 
            telefone='19966663333', 
            email='alexandre.gmail.com'
        )


def test_criar_cliente(lista_clientes):
    """Cria uma instância válida da classe Cliente"""    
    exemplo = lista_clientes[0]

    assert isinstance(exemplo.nome, str) # Verifica se é do tipo "str"
    assert isinstance(exemplo.cpf, str)
    assert isinstance(exemplo.telefone, str) 
    assert isinstance(exemplo.email, str) 
    assert exemplo.nome == 'Andre Conforti' # Verifica se foi inicializado corretamente
    assert exemplo.cpf == '27875969832'
    assert exemplo.telefone == '19988377497'
    assert exemplo.email == 'andre@gmail.com'