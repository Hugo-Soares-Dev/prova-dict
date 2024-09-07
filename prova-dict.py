"""Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
O programa deve fornecer as seguintes funcionalidades:
Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
O programa deve ser executado em um loop contínuo até que o usuário escolha sair."""

alunos = {}

while True:
    menu = input('Para adicionar um novo aluno digite(A)\nPara Remover um aluno digite (R)\nPara lista de alunos digite (L)\n Para Sair digite (S):\n-->').upper().strip()
    if menu == 'S':
        break
    elif menu == 'A':
        nome = input('digite o nome do aluno: ')
        matricula = int(input('digite o numero da matricula: '))
        if nome in alunos:
            menu2 = input('existe um cadastro com este nome, deseja substiuilo? (S/N): ').upper().strip()
            if menu2 != 'S':
                continue
            else:
                alunos[nome] = matricula
                print(f'aluno {nome} cadastrado substituido com sucesso!')
        elif matricula in alunos.values():
            print('este numero de matricula ja foi cadastrado, tente novamente')
            continue        
        else:
             alunos[nome] = matricula 
             print(f'aluno {nome} foi cadastrado com sucesso!')
    elif menu == 'L':
        for aluno, matricula in alunos.items():
            print(f'Aluno:{aluno.capitalize()} Mat:{matricula}\n') 
    elif menu == 'R':
        valor = int(input('para excluir um aluno digite o numero da matricula: '))
        chave = None
        for aluno, matricula in alunos.items():
            if matricula == valor:
                chave = aluno
                menu3 = input(f'({aluno.capitalize()}) sera excluido, deseja continuar? (S/N): ').upper().strip ()
                if menu3 != 'S':
                    continue
                elif menu3 == 'S':
                    del(alunos[chave])
                    print('cadastro excluido com sucesso!')
                break    
        if matricula != valor:
                print('matricula nao encontrada!')
print('Programa encerrado!')
        