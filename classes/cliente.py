from pydantic import BaseModel, EmailStr, validator


class Cliente(BaseModel):

    nome : str
    cpf : str
    telefone : str
    email : EmailStr 

    @validator('nome')
    def verifica_nome(cls, value):
        """Verifica se o nome do cliente contém apenas letras e espaços em branco para separar nome e sobrenome e para verificar se não contém números"""
        for letra in value:
            if letra.isdigit():
                raise ValueError('Nome inválido. Utilizar somente letras e espaços embranco para separar nome e sobrenome.')
            if not letra.isalpha() and not letra.isspace():
                raise ValueError('Nome inválido. Utilizar somente letras e espaços embranco para separar nome e sobrenome.')
        
        if value == '':
            raise ValueError('Nome inválido. Utilizar somente letras e espaços embranco para separar nome e sobrenome.')
        return value
    
    @validator('cpf')
    def verifica_cpf(cls, value):
        """Verifica se o cpf do cliente possui apenas números, formatado para não conter '-', '.' e espaços em branco"""
        for numero in value:
            if not numero.isdigit():
                raise ValueError('CPF inválido. Utilizar apenas números, sem caracteres especiais.')
        return value
    
    @validator('telefone')
    def verifica_telefone(cls, value):
        """Verifica se o telefone do cliente possui apenas números, já formatado para não conter '-', e espaços em branco """
        for numero in value:
            if not numero.isdigit():
                raise ValueError('Telefone inválido. Utilize apenas números.')
        return value

    @validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('E-mail inválido. Verifique seu valor.')
        return value
    
'''
# ====================================================================
if __name__ == '__main__':
    cliente = Cliente('Andre Conforti', '278.759.698-32', '19 988377497', 'andre.conforti@gmail.com')

    nome_valido = cliente.verifica_nome()
    telefone_valido = cliente.verifica_telefone()
    cpf_valido = cliente.verifica_cpf()

    if nome_valido and telefone_valido and cpf_valido:
        print("As informações sobre o cliente estão corretas.")
        # Se as informações estiverem corretas, deve-se então armazená-las no banco de dados
    else:
        print("Informações incorretas. Verifique e tente novamente!")

'''