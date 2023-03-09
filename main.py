import sys
import json
from classes.agenda import Agenda
from classes.reserva import Reserva
from classes.cliente import Cliente

# Cria a instância de Agenda
agenda = Agenda()

# Opção 1 = Verificar Quadra Disponível
def quadra_disponivel():
    # Parâmetros
    data=input('Digite a data no formato yyyy-mm-dd:')
    hora_ini=input('Informe horário de início:')
    duracao=input('Informe duração desejada (1 ou 3):')

    # Chamada
    quadras = agenda.quadra_disponivel (data, hora_ini, duracao)
    
    # Retorno
    print('----------------------------------------------------------------')
    if not quadras:            
        print('Nenhuma quadra disponível neste horário!')
    else:
        for quadra in quadras:
            print ('Quadras disponíveis:', quadra.nome_quadra)
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')

# Opção 2 = Consultar Agendamentos Cliente
def reservas_cliente():
    # Parâmetros
    nome=input('Informe o nome do cliente:')

    # Chamada
    reservas = agenda.reservas_cliente (nome)

    # Retorno
    print('----------------------------------------------------------------')
    if not reservas:
        print('Nenhuma reserva localizada!')
    else:
        #for reserva in reservas:
        #    print ('Reservas realizadas:', reserva)
        count_res = 1
        for reserva in reservas:
            print('----------------------------------------------------------------')
            print (f'Reserva {count_res}:')
            print(f'{reserva.quadra.nome_quadra} - dia {reserva.data}, das {reserva.hora_inicio}h até {reserva.hora_fim()}h, {reserva.duracao} hora(s).')
            if reserva.data_pago != None:
                print(f'Pagamento realizado em: {reserva.data_pago}')
            else:
                print(f'Pagamento pendente.')

            reserva_dict = vars(reserva.cliente)
            print(f'''Cliente: {json.dumps(reserva_dict, indent=4)}''')
            
            count_res += 1
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')

# Opção 3 = Reservar quadra para cliente
def agendar():
    # Parâmetros
    print('Dados Cliente:')
    nome=input('Informe o nome do cliente:')
    cpf=input('Informe o CPF do cliente:')
    telefone=input('Informe o telefone do cliente:')
    email=input('Informe o e-mail do cliente:')
    print('Dados do Agendamento:')
    data=input('Digite a data no formato yyyy-mm-dd:')
    hora_ini=input('Informe horário de início:')
    duracao=input('Informe duração desejada (1 ou 3):')
    try:    # Adiciona cliente validando os valores informados
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
    except ValueError as e:
        print(str(e))
        return

    # Chamada
    quadra = agenda.agendar(cliente=cliente, data=data, hora_ini=hora_ini, duracao=duracao)

    # Retorno
    if quadra:
        print(f'Quadra [{quadra.nome_quadra}] reservada com sucesso!')
    else:
        print(f'Nenhuma quadra disponível neste horário')


# Opção 4 = Cancelar quadra para cliente
def cancelar_reserva():
    # Parâmetros
    print('Dados da reserva:')
    data=input('Digite a data no formato yyyy-mm-dd:')
    hora_ini=input('Informe horário de início:')

    # Chamada
    reserva = agenda.cancelar_reserva(data=data, hora_inicio=hora_ini)

    # Retorno
    if reserva:
        print(f'Reserva cancelada com sucesso!')
    else:
        print(f'Nenhuma reserva encontrada neste horário')


# Opção 5 = Cancelar quadra para cliente
def pagar_reserva():
    # Parâmetros
    print('Dados da reserva:')
    data=input('Digite a data no formato yyyy-mm-dd:')
    hora_ini=input('Informe horário de início:')
    print('Dados pagamento:')
    data_pago = input('Digite a data de pagamento no formato yyyy-mm-dd:')

    # Chamada
    reserva = agenda.pagar_reserva(data=data, hora_inicio=hora_ini, data_pago=data_pago)

    # Retorno
    if reserva:
        print(f'Reserva paga com sucesso!')
    else:
        print(f'Nenhuma reserva encontrada neste horário')


# Opção 6 = Consultar Débito Cliente
def debitos_cliente():
    # Parâmetros
    nome=input('Informe o nome do cliente:')

    # Chamada
    reservas = agenda.reservas_cliente (nome)

    # Retorno
    print('----------------------------------------------------------------')
    if not reservas:
        print('Nenhuma reserva localizada!')
    else:
        #for reserva in reservas:
        #    print ('Reservas realizadas:', reserva)
        count_res = 0
        debito = 0
        for reserva in reservas:
            if reserva.data_pago == None:
                debito += reserva.valor_reserva()
                count_res += 1

        print('----------------------------------------------------------------')
        if debito>0:
            print (f'Reservas com débito: {count_res}')
            print (f'Valor total do débito {debito}')
           
        else:
            print ('Nenhum débito encontrado.')

        print('----------------------------------------------------------------')
        print('----------------------------------------------------------------')


def menu_option(opt):
    
    if not isinstance(opt, int):
        return 0
    
    if opt == 1:
        quadra_disponivel()

    if opt == 2:
        reservas_cliente()

    if opt == 3:
        agendar()

    if opt == 4:
        cancelar_reserva()

    if opt == 5:
        pagar_reserva()

    if opt == 6:
        debitos_cliente()
    
    return opt


# Verifica se há alguma opção inicial selecionada
if len(sys.argv) == 1:
    opt = 0
    print ('Olá! Parece que você não escolheu nenhuma opção válida!')
else:
    opt = int(sys.argv[1])



while (opt != 7):

    opt = menu_option(opt)
    
    # Menu:
    print ('''
    Temos as seguintes opções:

    1 - Consultar Disponibilidade (Informar: Quadra, Data/Hora, Duração) - retornará Hora e Cliente se já houver reserva
    2 - Consultar Agendamento Cliente (Informar: Cliente) - retornará quadra, data e horário agendado
    3 - Agendar (Informar: Cliente, Quadra, Data/Hora, Duração) - retornará sucesso ou hora e cliente ocupado
    4 - Cancelar (Informar: Cliente, Quadra, Data/Hora) - retornará sucesso dos horários cancelados ou negativa
    5 - Pagamento (Informa: Cliente, Quadra, Data/Hora) - retornará sucesso da operação
    6 - Debito (Informar: Cliente, Periodo) - retornará o valor do débito
    7 - Sair

        ''')

    opt = int(input("Digite sua opção: "))

    
   
agenda.save_agenda()
print ('Obrigado por utilizar nossos serviços!')





    


    