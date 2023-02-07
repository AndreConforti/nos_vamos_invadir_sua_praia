class Cliente():
    """Classe criada para identificar o cliente que será cadastrado para alugar uma quadra"""
    def __init__(self, nome, cpf, telefone, email, agendas=[]):
        self.nome = nome
        self.cpf = cpf.replace('-', '').replace('.', '').replace(' ', '').strip()
        self.telefone = telefone.replace('-', '').replace('.', '').replace(' ', '').strip()
        self.email = email
        self.agendas = agendas


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

