from agenda import Agenda, ReservaDuplicada
from quadra import Quadra, HorarioForaDoFuncionamento
from cliente import Cliente
import os
import csv

def recuperar_clientes(filename='clientes.csv'):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        clientes = [row for row in reader]
        return clientes



def main():

    quadra1 = Quadra(nome='Quadra 1', hora_inicio='10', hora_fim='22')
    quadra2 = Quadra(nome='Quadra 2', hora_inicio='10', hora_fim='22')
    quadra3 = Quadra(nome='Quadra 3', hora_inicio='10', hora_fim='22')
    quadra4 = Quadra(nome='Quadra 4', hora_inicio='10', hora_fim='22')

    agenda = Agenda()

    while True:
        os.system('clear' or None)
        opc = int(input('''
    BREACH TENNIS
    
    Escolha uma opção:
    
    1 - Cadastrar Cliente
    2 - Consultar Cliente
    3 - Agendar Quadra
    4 - Consultar Agenda
    5 - Cancelar Agendamento
    6 - Sair

    ''' ))

        if opc == 1:
            try:
                os.system('clear' or None)
                nome = input('Nome: ')
                cpf = input('CPF: ')
                telefone = input('Telefone: ')
                email = input('E-mail: ')
                saldo = 0

                cliente = Cliente(nome, cpf, telefone, email, saldo)
                cliente.gravar_clientes(nome, cpf, telefone, email, saldo)
                print('Cliente cadastrado')
            except:
                print('Não foi possível gravas os dados. Tente novamente')

            input()


        elif opc == 2:
            os.system('clear' or None)
            lista_clientes = recuperar_clientes()
            nome = input('Nome: ')
            find = False
            for registro in lista_clientes:
                if nome in registro['nome']:
                    print(registro)
                    find = True
            if find == False:
                print("Nenhum registro encontrado")
            input()

        elif opc == 3:
            os.system('clear' or None)
            quadra = int(input('Selecione a quadra: (1, 2, 3 ou 4) '))
            data = input('informa a data (yyyy-mm-dd): ')
            hora_inicio = input('Informe o início: ')
            hora_fim = input('Informe o término: ')
            nome = input('Nome do cliente: ')
            if quadra == 1:
                try:
                    quadra1.agendar(data, hora_inicio, hora_fim)      
                    agenda.confirmar_reserva(nome, data, hora_inicio, hora_fim)
                except HorarioForaDoFuncionamento as e:
                    print(e)
                except ReservaDuplicada as e:
                    print(e)
            if quadra == 2:
                try:
                    quadra2.agendar(data, hora_inicio, hora_fim)      
                    agenda.confirmar_reserva(nome, data, hora_inicio, hora_fim)
                except HorarioForaDoFuncionamento as e:
                    print(e)
                except ReservaDuplicada as e:
                    print(e)
            if quadra == 3:
                try:
                    quadra3.agendar(data, hora_inicio, hora_fim)      
                    agenda.confirmar_reserva(nome, data, hora_inicio, hora_fim)
                except HorarioForaDoFuncionamento as e:
                    print(e)
                except ReservaDuplicada as e:
                    print(e)
            if quadra == 4:
                try:
                    quadra4.agendar(data, hora_inicio, hora_fim)      
                    agenda.confirmar_reserva(nome, data, hora_inicio, hora_fim)
                except HorarioForaDoFuncionamento as e:
                    print(e)
                except ReservaDuplicada as e:
                    print(e)
            else:
                print('Opção inválida')

            input()

        elif opc == 4:
            os.system('clear' or None)
            lista_reservas = agenda.recuperar_reservas()
            for registro in lista_reservas:
                print(registro)
            
            input()


        elif opc ==5:
            os.system('clear' or None)


        elif opc == 6:
            break




main()



























# cliente = Cliente(
#     nome='Andre Conforti',
#     cpf='278.759.698-32',
#     telefone='19 98837-7497',
#     email='andre.conforti@gmail.com'
# )



# quadra1 = Quadra(nome='Quadra 1', hora_inicio='10', hora_fim='22')
# quadra2 = Quadra(nome='Quadra 2', hora_inicio='10', hora_fim='22')
# quadra3 = Quadra(nome='Quadra 3', hora_inicio='10', hora_fim='22')
# quadra4 = Quadra(nome='Quadra 4', hora_inicio='10', hora_fim='22')

# agenda = Agenda()

# try:
#     agendar = quadra1.agendar('2023-02-07', '10', '11')
#     confirma = agenda.confirmar_reserva(cliente.nome, '2023-02-07', '10', '11')
# except HorarioForaDoFuncionamento as e:
#     print(e)

# cliente.gravar_clientes(cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.saldo)





# cliente = Cliente(
#     nome='Ricardo Martins',
#     cpf='278.759.698-32',
#     telefone='19 99999-8888',
#     email='xxxxxx.xxxxxxxx@gmail.com'
# )

# try:
#     agendar = quadra1.agendar('2023-02-07', '18', '19')
#     confirma = agenda.confirmar_reserva(cliente.nome, '2023-02-07', '20', '21')
# except HorarioForaDoFuncionamento as e:
#     print(e)



# teste = agenda.recuperar_reservas()



# agenda.consultar_cliente(cliente.nome)

# # agenda.consultar_reservas_duplicadas(quadra1.nome, data='2023-02-07', hora_inicio='10', hora_fim='11')

# agenda.cancelar_reserva(cliente.nome, quadra1.nome, data='2023-02-07', hora_inicio='20', hora_fim='21')

# cliente.gravar_clientes(cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.saldo)














# while True:
#     try:
#         data = input('Informe a data (yyyy-mm-dd): ')
#         hora_inicio = input('Informe a hora de início: ')
#         hora_fim = input('Informe a hora de término: ')
#         disponivel = agenda.verificar_disponibilidade(data, hora_inicio, hora_fim)
#         if disponivel == []:
#             print("Nenhuma quadra disponível")
#         else:
#             print("Quadras disponíveis nesse horário: \n")
#             for quadra in disponivel:
#                 print(quadra.nome)
#             break
#     except HorarioForaDoFuncionamento as e:
#         print('Erro: ' + str(e))