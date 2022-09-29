from Módulos.funs import *
from Módulos.listas import *
from Módulos.colors import *

while True:

    print('DIGITE ENTER PARA ENTRAR...', end=' ')
    resp_0 = input('')

    if resp_0 == '':
        clean()
        music('Sons/gta.mp3')
        break

    else:
        clean()
clean()
lin_0()
lin2_30()

blue('   CADASTRO DE ESTUDANTES')
ast30()

sleep(3)
clean()

while True:

    tabela_estudantes = pd.DataFrame(estudantes)

    clean()
    print('DIGITE \033[32;1m[1]\033[m PARA CADASTRAR UM', end=' ')
    white('NOVO ESTUDANTE')

    print('DIGITE \033[32;1m[2]\033[m PARA EXCLUIR', end=' ')
    white('UM ESTUDANTE')

    print('DIGITE \033[32;1m[3]\033[m PARA VISUALIZAR', end=' ')
    white('INFORMAÇÕES DOS ESTUDANTES')

    lin2_30()
    lin_0()

    resp_p = input('--> ')

    if resp_p == '1':
        music('Sons/gta.mp3')
        clean()

        nome_e = input('DIGITE O NOME DO ESTUDANTE: ').upper().strip()
        idade_e = int(input('DIGITE A IDADE DO ESTUDANTE: '))

        while True:
            nota1_e = float(input('DIGITE A 1° NOTA DO ESTUDANTE: [0 À 10] '))
            nota2_e = float(input('DIGITE A 2° NOTA DO ALUNO: '))

            if nota1_e > 10 or nota2_e > 10:
                music('Sons/erro.mp3')
                lin_0()

                red('DIGITE NÚMEROS IGUAIS OU MENORES A 10!')
                clean()
                lin_0()

            else:
                break

        lin_0()
        green('VOCÊ DESEJA ADICIONAR ESSAS INFORMAÇÕES? [S/N]')
        lin_0()

        while True:
            resp_e = input('--> ').strip().upper()

            if resp_e == 'S':
                music('Sons/gta.mp3')
                clean()

                estudantes["NOMES"].append(nome_e)
                estudantes["IDADES"].append(idade_e)

                media = (nota1_e + nota2_e) / 2
                estudantes["NOTAS"].append(media)

                green('INFORMAÇÕES ADICIONADAS COM SUCESSO!')
                sleep(3)

                break

            elif resp_e == 'N':
                music('Sons/erro.mp3')
                clean()
                break

            else:
                music('Sons/erro.mp3')
                clean()
                red('OPÇÃO INVÁLIDA TENTE NOVAMENTE!')
                lin_0()

    if resp_p == '2':
        clean()
        while True:

            if len(estudantes["NOMES"]) == 0:
                music('Sons/erro.mp3')
                lin_0()
                red('VOCÊ NÃO CADASTROU NENHUM ESTUDANTE!')
                sleep(3)
                break

            else:
                music('Sons/gta.mp3')
                clean()

                red('DIGITE O NÚMERO DO ESTUDANTE EM QUE DESEJA EXCLUIR.')
                lin_0()

                print(tabela_estudantes)
                lin_0()
                while True:
                    print('--> ', end='')
                    estudante_excluido = int(input(''))

                    if estudante_excluido > len(estudantes["NOMES"]):
                        lin_0()
                        red('NÚMERO INVÁLIDO!')
                        lin_0()

                    else:
                        break

                clean()
                print(f'\033[97;1mVOCÊ DESEJA EXCLUIR O ESTUDANTE\033[m \033[34;1mNÚMERO {estudante_excluido}\033[m [S/N]')

                lin_0()
                resp_e2 = input('--> ').strip().upper()

                if resp_e2 == 'S':
                    music('Sons/gta.mp3')
                    clean()

                    estudantes["NOMES"].pop(estudante_excluido)
                    estudantes["IDADES"].pop(estudante_excluido)
                    estudantes["NOTAS"].pop(estudante_excluido)

                    green('ESTUDANTE EXCLUIDO COM SUCESSO!')
                    sleep(2)
                    break

                if resp_e2 == 'N':
                    music('Sons/erro.mp3')
                    clean()
                    lin_0()
                    red('ESTUDANTE NÃO EXCLUIDO!')
                    sleep(2)
                    break

                else:
                    music('Sons/erro.mp3')
                    clean()
                    red('DIGITE APENAS S OU N')
                    lin_0()

    if resp_p == '3':

        while True:

            if len(estudantes["NOMES"]) == 0:
                clean()
                lin_0()
                music('Sons/erro.mp3')
                red('VOCÊ NÃO CADASTROU NENHUM ESTUDANTE!')
                sleep(3)
                break

            else:
                music('Sons/gta.mp3')
                clean()
                lin_0()

                print(f'{tabela_estudantes}')

                if len(estudantes["NOTAS"]) > 1:
                    media_estudantes = (sum(estudantes["NOTAS"])) / len(estudantes["NOTAS"])
                    lin30()
                    green(f'MÉDIA DE NOTAS: {round(media_estudantes, 2)}')

                lin_0()
                lin_0()
                print('\033[31;1mDIGITE ENTER PARA SAIR...\033[m', end=' ')
                r3_s = input('')

                if r3_s == '':
                    music('Sons/erro.mp3')
                    clean()
                    break

                else:
                    clean()
