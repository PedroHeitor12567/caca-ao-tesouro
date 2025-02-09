import random
from colorama import Fore, Back, Style


linhas = 5
colunas = 5

treasure_row = random.randint(0, linhas - 1)
treasure_col = random.randint(0, colunas - 1)

print(Fore.YELLOW + "*****************")
print("*Caça ao Tesouro*")
print("*****************")

while True:
    print(Fore.WHITE + "Nível 3: 5 tentativas \nNível 2: 10 tentativas \nNível 1: 15 tentativas\n")
    dificuldade = int(input("Escolha o nível: "))
    if dificuldade == 1:
        tentativas_restantes = 15
        break
    elif dificuldade == 2:
        tentativas_restantes = 10
        break
    elif dificuldade == 3:
        tentativas_restantes = 5
        break
    else:
        print("Nível inválido, escolha entre 1, 2 ou 3")
        continue

print(f"Você tem que encontrar o tesouro numa grade 5x5 com apenas {tentativas_restantes} tentativas, deve inserir o número da linha e da coluna separadamente")

tentativas = set()
encontrar = False

while not encontrar and tentativas_restantes > 0:
    try:        
        print(Fore.WHITE + "\nGrade Atual")
        print(Fore.CYAN + "   1   2   3   4   5")
        for i in range(linhas):
            print(Fore.CYAN + f"{i + 1}", end=" ")
            for j in range(colunas):
                if (i, j) in tentativas:
                    print(Fore.RED + "[X]", end=" ")
                else:
                    print(Fore.BLUE + "[ ]", end=" ")
            print()
        
        resp_coluna = int(input(Fore.WHITE + "Digite um número para a coluna de 1 a 5: ")) - 1
        resp_linha = int(input("Digite um número para a linha de 1 a 5: ")) - 1
        
        if resp_linha < 0 or resp_linha >= linhas or resp_coluna < 0 or resp_coluna >= colunas:
            print(Fore.RED + "Número inserido fora dos limites da grade, insira um valor entre 1 e 5.")
            continue
        
        tentativas.add((resp_linha, resp_coluna))    
        tentativas_restantes -= 1
        
        if resp_linha == treasure_row and resp_coluna == treasure_col:
            print(Fore.GREEN + f"Parabéns, você encontrou o tesouro em {tentativas_restantes} tentativa(s)!")
            encontrar = True
        else:
            if resp_coluna < treasure_col:
                print(Fore.MAGENTA + "O tesouro está mais para a direita")
            elif resp_coluna > treasure_col:
                print(Fore.MAGENTA + "O tesouro está mais para a esquerda")
            if resp_linha > treasure_row:
                print(Fore.MAGENTA + "O tesouro está mais para cima")
            elif resp_linha < treasure_row:
                print(Fore.MAGENTA + "O tesouro está mais para baixo")    

            print(Fore.RED + f"Não está aqui, continue procurando! Você ainda possui {tentativas_restantes} tentativa(s)")

    except ValueError:
        print("Entrada inválida! Por favor, insira números inteiros para a linha e coluna.")
    
if not encontrar:
    print(f"\nVocê não encontrou o tesouro, na próxima você se dará melhor! O tesouro estava na posição ({treasure_col + 1, treasure_row + 1})")

print(Fore.WHITE + "\nGrade Final")
print(Fore.CYAN + "   1   2   3   4   5")
for i in range(linhas):
    print(Fore.CYAN + f"{i + 1}", end=" ")
    for j in range(colunas):
        if (i, j) == (treasure_row, treasure_col):
            print(Fore.GREEN + "[T]", end=" ")
        elif (i, j) in tentativas:
            print(Fore.RED + "[X]", end=" ")
        else:
            print(Fore.BLUE + "[ ]", end=" ")
    print()
