print('--'*20)
print('ESSE É O QUIZ DE FUTEBOL')
confirmation = input('VOCÊ QUER INICIAR? [S/N]: ')
print('--'*20)

SCORE = 0

if confirmation != 'S':
    quit()

print('Qual país venceu a Copa do Mundo da FIFA em 2018? \n a) Alemanha b) Brasil c) França d) Argentina \n')
r1 = input('QUAL É A ALTERNATIVA CORRETA: ')
if r1 == 'C':
    print(f'VOCÊ ESCOLHEU {r1} E ACERTOU!!!')
    SCORE += 1
else:
    print('RESPOSTA INCORRETA!')

print('--'*20)

print('Qual jogador é conhecido como "El Fenômeno"?\n a) Lionel Messi b) Cristiano Ronaldo c) Ronaldinho d) Ronaldo (Ronaldo Luís Nazário de Lima) \n')
r2 = input('QUAL A ALTERNATIVA CORRETA: ')
if r2 == 'D':
    print(f'VOCÊ ESCOLHEU {r2} E ACERTOU!!!')
    SCORE +=1
else:
    print('RESPOSTA INCORRETA! \n')

print('--'*20)
if SCORE == 0:
    print('--'*20)
    print('VOCÊ NÃO ACERTOU NENHUMA')
else:
    print(f'VOCÊ ACERTOU UM TOTAL DE {SCORE}/2')
    print('--'*20)
