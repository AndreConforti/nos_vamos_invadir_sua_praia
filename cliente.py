import csv
import os


class Cliente():
    """Classe criada para identificar o cliente que será cadastrado para alugar uma quadra"""
    def __init__(self, nome, cpf, telefone, email, saldo=0):
        self.nome = nome
        self.cpf = cpf.replace('-', '').replace('.', '').replace(' ', '').strip()
        self.telefone = telefone.replace('-', '').replace('.', '').replace(' ', '').strip()
        self.email = email
        self.saldo = saldo
        self.clientes = []


    def veririca_nome(self):
        """Verifica se o nome do cliente contém apenas letras e espaços em branco para separar nome e sobrenome e para verificar se não contém números"""
        for letra in self.nome:
            if letra.isdigit():
                return False
            if not letra.isalpha() and not letra.isspace():
                return False
        
        if self.nome == '':
            return False
        return True


    def verifica_telefone(self):
        """Verifica se o telefone do cliente possui apenas números, já formatado para não conter '-', e espaços em branco """
        for numero in self.telefone:
            if not numero.isdigit():
                return False
        return True


    def verifica_cpf(self):
        """Verifica se o cpf do cliente possui apenas números, formatado para não conter '-', '.' e espaços em branco"""
        for numero in self.cpf:
            if not numero.isdigit():
                return False
        return True


    def verifica_agenda(self, horario):
        for agenda in self.agendas:
            if agenda.esta_ocupado(horario):
                return True
        return False


    def gravar_clientes(self, nome, cpf, telefone, email, saldo, filename='clientes.csv'):
        clientes = self.recuperar_clientes()
        cliente = {
            'nome'     : nome,
            'cpf'      : cpf,
            'telefone' : telefone,
            'email'    : email,
            'saldo'    : saldo 
        }
        clientes.append(cliente.copy())
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['nome', 'cpf', 'telefone', 'email', 'saldo']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for cliente in clientes:
                writer.writerow(cliente)


    def recuperar_clientes(self, filename='clientes.csv'):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            clientes = [row for row in reader]
            return clientes