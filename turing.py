def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = "Em junho de 1938, ele obteve seu doutorado no Departamento de Matemática de Princeton; sua dissertação, Systems of Logic Based on Ordinals, introduziu o conceito de lógica ordinal e a noção de computação relativa"
    return mensagem


def contribuicoes():
    mensagem = "Turing trabalhou na decidibilidade de problemas, partindo dos teoremas da incompletude de Gödel, construiu três dos quatro estágios de um multiplicador binário eletromecânico. Turing foi um dos principais participantes na quebra de cifras alemãs em Bletchley Park."
    return mensagem


def artigos():
    mensagem = "Equivalência de quase periodicidade esquerda e direita, The Applications of Probability to Cryptography, Paper on Statistics of Repetitions"
    return mensagem


def citacoes():
    mensagem = f'Algumas frases de Alan Turing são:\n"As máquinas me surpreendem muito frequentemente"\n"Nós só podemos ver um pouco do futuro, mas o suficiente para perceber que há muito a fazer."\n"Eu acredito que às vezes são as pessoas que ninguém espera nada que fazem as coisas que ninguém consegue imaginar."'
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
