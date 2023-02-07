import pytest
from cliente import Cliente


def test_criar_cliente():
    exemplo = Cliente('André Conforti', '278.759.698-32', '19 988377497', 'Rua José Adami, 485 - Santa Marta - Leme')

    assert isinstance(exemplo.nome, str) # Verifica se é do tipo "str"
    assert isinstance(exemplo.cpf, str)
    assert isinstance(exemplo.telefone, str) 
    assert isinstance(exemplo.endereco, str) 
    assert exemplo.nome == 'André Conforti' # Verifica se foi inicializado corretamente
    assert exemplo.cpf == '27875969832'
    assert exemplo.telefone == '19988377497'
    assert exemplo.endereco == 'Rua José Adami, 485 - Santa Marta - Leme'


def test_alterar_campo():
    exemplo = Cliente('André Conforti', '278.759.698-32', '19 988377497', 'Rua José Adami, 485 - Santa Marta - Leme')

    exemplo.nome = 'Ricardo Martins' # Altera os valores 
    exemplo.cpf = '98545896347'
    exemplo.telefone = '11988887777'
    exemplo.endereco = 'Av. 29 de Agosto, 1625 - Centro - Leme'
    assert exemplo.nome == 'Ricardo Martins' # Verifica se os novos valores foram alterados
    assert exemplo.cpf == '98545896347'
    assert exemplo.telefone == '11988887777'
    assert exemplo.endereco == 'Av. 29 de Agosto, 1625 - Centro - Leme'


def test_validar_nome():
    exemplo = Cliente('André Conforti', '278.759.698-32', '19 988377497', 'Rua José Adami, 485 - Santa Marta - Leme')

    exemplo.nome = ''
    assert exemplo.veririca_nome() == False # Verifica se não é vazio

    exemplo.nome = 'Andre123'
    assert exemplo.veririca_nome() == False # Verifica se possui números

    exemplo.nome = 'Ricardo Martins' 
    assert exemplo.veririca_nome() == True # Verifica se está correto


def test_validar_telefone():
    exemplo = Cliente('André Conforti', '278.759.698-32', '19 98837-7497', 'Rua José Adami, 485 - Santa Marta - Leme')

    assert exemplo.verifica_telefone() == True # Verifica se está correto

    exemplo.telefone = 'abcdefghijk'
    assert exemplo.verifica_telefone() == False # Verifica se possui letras

    exemplo.telefone = '19 98837 74AB'
    assert exemplo.verifica_telefone() == False # Verifica se possui letras e números

    exemplo.telefone = '19 98837 7499'
    assert exemplo.verifica_telefone() == False # Verifica se colocar um novo número com espaços


def test_validar_cpf():
    exemplo = Cliente('André Conforti', '278.759.698-32', '19 98837-7497', 'Rua José Adami, 485 - Santa Marta - Leme')

    assert exemplo.verifica_cpf() == True # Verifica se está correto

    exemplo.cpf = 'abc.def.ghi-jk'
    assert exemplo.verifica_cpf() == False # Verifica se possui letras

    exemplo.cpf = '278 859 abc 25'
    assert exemplo.verifica_cpf() == False # Verifica se possui letras e números


