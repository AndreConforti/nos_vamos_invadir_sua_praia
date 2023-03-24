# Nós vamos invadir sua praia!

Este é um projeto de agendamento de quadras esportivas de Beach Tennis em Python. O projeto utiliza orientação a objetos para modelar as entidades do sistema, como clientes, quadras e reservas, e uma classe Agenda para gerenciar o agendamento e disponibilidade das quadras.

O programa apresenta um menu com as seguintes opções:

* Verificar Quadra Disponível
* Consultar Agendamentos Cliente
* Reservar Quadra para Cliente
* Sair

Ao escolher uma das opções, o programa solicitará os dados necessários para realizar a operação. As opções disponíveis são:

### Verificar Quadra Disponível
Permite verificar a disponibilidade de uma quadra em um determinado dia e horário.

### Consultar Agendamentos Cliente
Permite consultar os agendamentos de um cliente em uma determinada quadra.

### Reservar Quadra para Cliente
Permite reservar uma quadra para um cliente em um determinado dia e horário.

### Sair
Encerra o programa

---
## classe Agenda
Este projeto implementa uma agenda para reservas de quadras de beach tênis. A agenda permite a marcação de reservas de acordo com a disponibilidade das quadras e horários.

A agenda é capaz de verificar as quadras disponíveis para uma determinada data e horário, garantindo que a reserva só seja confirmada se a quadra estiver livre naquele momento.

---
## classe Cliente
Classe Cliente
A classe Cliente é uma classe que representa um cliente com informações básicas, como nome, CPF, telefone e email. Ela é implementada utilizando a biblioteca Pydantic para validação de dados.

Se os valores fornecidos não forem válidos, a classe Pydantic lançará uma exceção ValidationError, indicando qual validação falhou e o motivo.

As validações realizadas pela classe Cliente são:
### Verificação de nome
Verifica se o nome do cliente contém apenas letras e espaços em branco para separar nome e sobrenome, e se não contém números;
### Verificação de CPF
Verifica se o CPF do cliente possui apenas números, formatado para não conter '-', '.' e espaços em branco;
### Verificação de telefone
Verifica se o telefone do cliente possui apenas números, já formatado para não conter '-' e espaços em branco;
### Verificação de email
Verifica se o email do cliente é válido, contendo um '@' e um domínio válido.

---
### classe Locacao
Esta é uma classe base para representar uma opção de locação. Possui um método get_locacao_info, que retorna uma string informando que a instância é uma opção de locação.

### classe Quadra_BeachTenis
Esta é uma classe derivada da classe Locacao, que representa uma opção de locação específica de uma quadra de Beach Tênis. Ela sobrescreve o método get_locacao_info da classe base, para retornar uma string informando sobre a quadra de Beach Tênis em específico. A classe também possui um método adicional drenagem, que retorna uma string informando se a quadra possui ou não sistema de drenagem.

---
### classe Reserva
A classe Reserva é responsável por representar uma reserva de uma quadra de Beach Tênis feita por um cliente.

A classe também define dois métodos:

#### hora_fim
Método que retorna a hora de término da reserva.
#### valor_reserva
Método que retorna o valor da reserva, calculado de acordo com a duração da reserva.
