import sys, os, keyboard
import json
from classes.agenda import Agenda
from classes.reserva import Reserva
from classes.cliente import Cliente

# Cria a instância de Agenda
agenda = Agenda()

def wait_key():
    # Solicitar que o usuário pressione qualquer tecla para continuar
    print("Pressione qualquer tecla para continuar...")

    # Esperar que o usuário pressione qualquer tecla
    keyboard.read_event()

# Opção 1 = Verificar Quadra Disponível
def quadra_disponivel():
    print('----------------------------------------------------------------')
    print('-- PESQUISA DE QUADRAS DISPONÍVEIS')
    # Parâmetros
    data=input('Digite a data no formato yyyy-mm-dd:')
    quadra_des=input('Informe a quadra desejada (1 a 4, ou 0 para qualquer quadra):')
    hora_ini=input('Informe horário de início:')
    duracao=input('Informe duração desejada (1 ou 3):')

    # Chamada
    quadras = agenda.quadra_disponivel (data, hora_ini, duracao, quadra_des)
    
    # Retorno
    print('----------------------------------------------------------------')
    if not quadras:            
        print('Quadra indisponível neste horário!')
    else:
        for quadra in quadras:
            print ('Quadras disponíveis:', quadra.nome_quadra)
    
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')

    wait_key()

# Opção 2 = Consultar Agendamentos Cliente
def reservas_cliente():

    print('----------------------------------------------------------------')
    print('-- PESQUISA RESERVAS DE CLIENTES')

    # Parâmetros
    nome=input('Informe o nome do cliente:')
    quadra_des=input('Informe a quadra desejada (1 a 4, ou 0 para qualquer quadra):')

    # Chamada
    reservas = agenda.reservas_cliente (nome, quadra_des)

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
    
    wait_key()

# Opção 3 = Reservar quadra para cliente
def agendar():
    print('----------------------------------------------------------------')
    print('-- AGENDAR UMA QUADRA')

    # Parâmetros
    print('Dados Cliente:')
    nome=input('Informe o nome do cliente:')
    cpf=input('Informe o CPF do cliente:')
    telefone=input('Informe o telefone do cliente:')
    email=input('Informe o e-mail do cliente:')
    print('Dados do Agendamento:')
    data=input('Digite a data no formato yyyy-mm-dd:')
    quadra_des=input('Informe a quadra desejada (1 a 4, ou 0 para qualquer quadra):')
    hora_ini=input('Informe horário de início:')
    duracao=input('Informe duração desejada (1 ou 3):')
    try:    # Adiciona cliente validando os valores informados
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
    except ValueError as e:
        print(str(e))
        return

    # Chamada
    quadra = agenda.agendar(cliente=cliente, data=data, hora_ini=hora_ini, duracao=duracao, quadra=quadra_des)

    # Retorno
    if quadra:
        print(f'Quadra [{quadra.nome_quadra}] reservada com sucesso!')
    else:
        print(f'Quadra indisponível neste horário')

    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')   

    wait_key()

# Opção 4 = Cancelar quadra para cliente
def cancelar_reserva():
    print('----------------------------------------------------------------')
    print('-- CANCELAR UMA RESERVA REALIZADA')

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

    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')   

    wait_key()

# Opção 5 = Cancelar quadra para cliente
def pagar_reserva():
    print('----------------------------------------------------------------')
    print('-- PAGAR UMA RESERVA')

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

    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')   

    wait_key()

# Opção 6 = Consultar Débito Cliente
def debitos_cliente():
    print('----------------------------------------------------------------')
    print('-- CONSULTAR DÉBITOS CLIENTE')

    # Parâmetros
    nome=input('Informe o nome do cliente:')

    count_res_week, debito_semana, count_res_month, debito_mes = agenda.debito_cliente(nome)

    # Retorno
    print('----------------------------------------------------------------')
    if count_res_week+count_res_month>0:

        print('----------------------------------------------------------------')
    
        print (f'Quantidade reservas com débito na semana atual: {count_res_week}')
        print (f'Valor total do débito da semana corrente: {debito_semana}')
        
        print (f'Quantidade reservas com débito no mês atual: {count_res_month}')
        print (f'Valor total do débito do mês corrente: {debito_mes}')

    else:
        print('Nenhum débito encontrado.')
        
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')   

    wait_key()


def menu_option(opt):
    
    os.system('cls' if os.name == 'nt' else 'clear')

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
    
    os.system('cls' if os.name == 'nt' else 'clear')

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





    


    