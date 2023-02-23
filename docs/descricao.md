## Projeto Nós vamos invadir sua praia

Seguir a ------ de Arquiterua Limpa
Como primeira tarefa, devemos identificar as entidades e suas principais funções dentro do programa.

* Cliente
* Quadra
* Agenda
* Aluguel

* Cliente
    - Nome
    - Telefone
    - CPF
    - Endereço (posteriormente pode ser desmembrado para incluir no banco de dados)

* Quadra
    - Número da quadra
    - hora_inicio (início durante a semana)
    - hora_fim (fim durante a semana)
    - Hora_inicio_domingo
    - hora_fim_domingo
    - tempo (1 ou 3 horas)
    - Horarios disponíveis {data : horarios} Dicionário contendo a agenda com as datas e horários
        
    - se o tempo for 3 horas pegamos 
        {'2023-02-03': ['08:00', '09:00', '10:00']}
        {'2023-02-04': ['09:00', '14:00']}
        por exemplo

