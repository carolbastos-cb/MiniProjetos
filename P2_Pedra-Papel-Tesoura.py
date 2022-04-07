'''
PEDRA, PAPEL OU TESOURA
'''

# entrada dos nomes dos jogadores
jogador_1 = input("Jogador 1, digite seu nome: ").title()
jogador_2 = input("Jogador 2, digite seu nome: ").title()

# define variável em branco para armazenar a escolha do jogador 1
escolha_j1 = ""

# entrada de dados para a escolha do jogador 1
while escolha_j1 not in ["PEDRA", "PAPEL", "TESOURA"]: # verifica se o jogador esta escolhendo uma das opções corretas
    print(f"{jogador_1}, faça sua escolha.")
    escolha_j1 = input("Pedra, Papel ou Tesoura: ").upper() # transforma todas as letras em maiúsculas
    if escolha_j1 not in ["PEDRA", "PAPEL", "TESOURA"]:
        print("Opção inválida.")
        
# define variável em branco para armazenar a escolha do jogador 2
escolha_j2 = ""
while escolha_j2 not in ["PEDRA", "PAPEL", "TESOURA"]:
    print(f"{jogador_2}, faça sua escolha.")
    escolha_j2 = input("Pedra, Papel ou Tesoura: ").upper()
    if escolha_j2 not in ["PEDRA", "PAPEL", "TESOURA"]:
        print("Opção inválida.")

# exibe as escolhas de cada jogador
print(f"{jogador_1} -> {escolha_j1}")
print(f"{jogador_2} -> {escolha_j2}")

# verifica quem ganhou
if escolha_j1 == escolha_j2:
    print("Empate.")
elif escolha_j1 == "PEDRA" and escolha_j2 == "TESOURA" or escolha_j1 == "TESOURA" and escolha_j2 == "PAPEL" or escolha_j1 == "PAPEL" and escolha_j2 == "PEDRA":
    print(f"Vitória de {jogador_1}!!!")
else:
    print(f"Vitória de {jogador_2}!!!")
