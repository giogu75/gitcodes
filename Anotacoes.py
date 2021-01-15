# ┌───────────┐
# │ MODULO 02 │
# └───────────┘

# ┌───────────┐
# │ VARIÁVEIS │
# └───────────┘

# -Numeros:

import random
from datetime import datetime
import math
velocidade_internet = 10
print(velocidade_internet)
# >10 - ->int
print('──────────────────────────────────────────────────────────────────────')
variavel_1 = 25, 43
# > float
print('──────────────────────────────────────────────────────────────────────')
# Valores boleanos:

esta_aberta = True  # /false
print('──────────────────────────────────────────────────────────────────────')

# Strings:

slogan = 'feito é melhor que perfeito!'
slogan = "feito é melhor que perfeito!"
print('──────────────────────────────────────────────────────────────────────')
a, b, c, d = 1, 2, 3, 4
print(a)
print(b)
print(c)
print(d)
# >1
# >2
# >3
# >4
print('──────────────────────────────────────────────────────────────────────')
print(type(a))
print(type(velocidade_internet))
# >class 'int'
# >class 'int'
print('──────────────────────────────────────────────────────────────────────')


# ┌────────────┐
# │ INDENTAÇÃO │
# └────────────┘

if 10 > 5:
    print('10 é maior que 5')


class BemVindo():
    def __init__(self):
        print('bem vindo')


oi = BemVindo()


def PensarPor10Segundos():
    print('pensando')
    time.sleep(10)
    print('lembrei')


print('──────────────────────────────────────────────────────────────────────')


# ┌─────────┐
# │ STRINGS │
# └─────────┘

print('Codar todos os dias!')
print("Codar todos os dias!")
print('''estamos codando todos os dias
    e estou aprendendo muito''')
print('──────────────────────────────────────────────────────────────────────')


# ┌──────────────────────┐
# │ CARACTERES DE ESCAPE │
# └──────────────────────┘

print('ola meu nome é \nGiovani')  # --> quebra de linha
print('arquivo localzado em \\ c:drive\\ arquivo1.txt')
print('──────────────────────────────────────────────────────────────────────')

nome = 'carol'
print(len(nome))
print('──────────────────────────────────────────────────────────────────────')

print('vamos \n "codar"')
# >Vamos
# >"codar"
print('──────────────────────────────────────────────────────────────────────')


# ┌───────────────────┐
# │ STRINGS DINÂMICOS │
# └───────────────────┘

print('──────────────────────────────────────────────────────────────────────')
nome = 'rafael'
email = 'rafael@gmail.com'
print(f'olá {nome}, vc cadastrou o email {email}, essa inrformação está correta?')
print('──────────────────────────────────────────────────────────────────────')
nome = 'Carol'
hobby = 'ouvir musica'
print(f'Olá eu sou {nome}, e gosto de {hobby}!')
print('──────────────────────────────────────────────────────────────────────')

b = 'ba'
parte_2 = 'nica'
a = 'a'
r = 'ri'
parte_1 = 'eletro'
t = 'te'
print(f'{b}{t}{r}{a} {parte_1}{parte_2}')
print('──────────────────────────────────────────────────────────────────────')

nome_curso = ' Edição de vídeo '
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find('ção'))
print(nome_curso.replace('vídeo', 'música'))
print('http://sc/olx.com.br/?o=90&q=relógio'.replace('relógio', 'carro'))
print('──────────────────────────────────────────────────────────────────────')

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'
print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
print('──────────────────────────────────────────────────────────────────────')

teclado = 'Teclado'
print(teclado[-1])
print(teclado.index('l'))
print(teclado[teclado.index('l')])
print('──────────────────────────────────────────────────────────────────────')


# ┌────────────────────────────────┐
# │ ACESSANDO PARTES DE UMA STRING │
# └────────────────────────────────┘

link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])
print('──────────────────────────────────────────────────────────────────────')

# encontre o indice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))
print('──────────────────────────────────────────────────────────────────────')

# imprima apenas 'De aplicações'
frase = 'Desenvolvimento De aplicações'
indice_d = frase.rindex('D')
indice_s = frase.rindex('s')
print(frase[indice_d:indice_s+1])
print('──────────────────────────────────────────────────────────────────────')


# ┌──────────────┐
# │ SPLIT E JOIN │
# └──────────────┘

frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
print('──────────────────────────────────────────────────────────────────────')

nomes = 'jonathan, rafael, carol, amanda, jefferson'
print(nomes.split())
print(nomes.split(','))
print('──────────────────────────────────────────────────────────────────────')

hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
print('──────────────────────────────────────────────────────────────────────')


# ┌────────────────────────────────────┐
# │ COMO CONCATENAR (COMBINAR) STRINGS │
# └────────────────────────────────────┘

hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print(', '.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))
print('──────────────────────────────────────────────────────────────────────')

""" DESAFIOS
Desafio 1: transforme a frase1 em uma lista de palavras
e guarde o resultado em uma variavel camada palavras1

Desafio 2: transforme a frase2 em uma lista de palavras
e guarde o resultado em uma variavel camada palavras2

Desafio 3: pegue o palavras1 e transforme elas no seguinte
string: "Desafio,manipulação,de,strins". imprima o resultado
no console.

Desafio 4: pegue o palavras2 e transforme elas no seguinte
string: "jhonatan & rafael & carol & camilla". imprima o resultado
no console. """
print('───────────────────────────────────────────────────────────────────────')
frase1 = 'Desafio manipulação de strings'
palavras1 = frase1.split()
print(palavras1)
print(','.join(palavras1))
print('──────────────────────────────────────────────────────────────────────')

frase2 = 'jhonatan,rafael,carol,camilla'
palavras2 = frase2.split(',')
print(palavras2)
print(' & '.join(palavras2))
print('──────────────────────────────────────────────────────────────────────')


# ┌───────────────────────────────────┐
# │ INPUT: RECEBENDO DADOS DO USUÁRIO │
# └───────────────────────────────────┘

""" senha = input("Digite sua senha: ")
print(senha)
print(type(senha))
print(
    '----------------------------------------------')
quantidade_de_filmes = int(
    input('Quantos filmes vc assistiu? '))
print(type(quantidade_de_filmes))
 """

# ┌────────────────────────────────┐
# │ NÚMEROS E OPERAÇÕES MATEMÁTICA │
# └────────────────────────────────┘

# alt+218 = ┌
# alt+217 = ┘
# alt+192 = └
# alt+191 = ┐
# alt+179 = │
# alt+196 = ─


""" Tipos de numeros que podem ser usados no Python: """
a = 20
b = 20.5
print(type(a))
print(type(b))
print('──────────────────────────────────────────────────────────────────────')

""" Operações Matemáticas: """
print(10 + 6)
print(10 - 6)
print(10 * 6)
print(10 / 6)
print(10 // 6)  # divisão de inteiros
print(10 % 6)  # modulus
print(10 ** 6)  # exponenciais
print('──────────────────────────────────────────────────────────────────────')

""" Atalho para atribuição mais rápida """
a = 10
a += 5   # a = a + 5
print(a)

b = 20
b -= 2  # b = b - 2
print(b)
print('──────────────────────────────────────────────────────────────────────')

''' Operações Matemáticas comuns '''
print(round(5.2))       # --> operação matemária comum: arredonda pra cima/baixo
print(round(5.3))       # --> operação matemária comum: arredonda pra cima/baixo
print(round(5.4))       # --> operação matemária comum: arredonda pra cima/baixo
print(round(5.5))       # --> operação matemária comum: arredonda pra cima/baixo
print(math.ceil(2.1))   # --> arredonda pra cima, próximo inteiro:
# http://docs.python.org/3/library/math.html
print('──────────────────────────────────────────────────────────────────────')


# ┌──────────────────┐
# │ DATETIME E TEMPO │
# └──────────────────┘

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print('──────────────────────────────────────────────────────────────────────')

''' Criar uma data '''
lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)
print('──────────────────────────────────────────────────────────────────────')

''' Quero receber a data de lançamento do meu aplicativo '''
''' 25/08/2020 
data_de_lancamento = datetime.strptime(input(
    'Quando devemos lançar o aplicativo? '), '%d/%m/%Y')
        # %Y = 2021; %y = 21 (abreviado)
print(type(data_de_lancamento))
dia = data_de_lancamento.day
mes = data_de_lancamento.month
ano = data_de_lancamento.year
print(f'Data de lançamento: {dia}/{mes}/{ano}') #formato brasileiro
data_Atual = datetime.now()
prazo = data_de_lancamento - data_Atual
print (f'Faltam {prazo.days} dias para o lançamento do app.')
print('───────────────────────────────────────────────────────────────────────')

Desafio
Calcule quantos dias faltam até o seu aniversário
dia_aniversário = datetime.strptime(input(
    'Qual a data do seu aniversário? '), '%d/%m/%Y')
dia_atual = datetime.now()
dia2 = (dia_aniversário) - (dia_atual)
print (f'Faltam {dia2.days} dias para o seu aniversário.')
'''


# ┌───────────────────────────────┐
# │ VALORES ALEATÓRIOS COM RANDOM │
# └───────────────────────────────┘


print(random.random())  # gera valor aleatorio de 0.0 a 1.0

# gera um valor decimal de valor mínimo ao valor máximo
print(random.uniform(4, 10))

# gera um valor inteiro de valor mínimo ao valor máximo
print(random.randint(4, 10))


cores = ['verde', 'vermelho', 'azul', 'preto', 'cinza', 'amarelo']
print(random.choice(cores))  # escolher opção aleatória
print(random.choices(cores, k=2))  # escolher 'duas' opção aleatória

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3']
print(random.choice(cartas_de_um_baralho))

lista = ['cara', 'coroa']  # jogo do cara e coroa
print(random.choice(lista))

nomes = ['nome', 'nome2', 'nome3', 'nome4', 'nome5']  # escolher um nome
print(random.choice(nomes))

print(random.randint(10, 100))  # escolher numnero entre 10 e 100


# ┌─────────────────────────┐
# │ COMO DEBUGAR SEU CÓDIGO │
# └─────────────────────────┘

# AULA 14
print('Ola')


def calcular_preço_combo(pizza, refrigerante):
    total = pizza + refrigerante
    print(f'Total: {total}')


calcular_preço_combo(30, 20)

print('Programa Finalizado')


# ┌──────────────────────────┐
# │ PROJETO 1 - CADASTRE-ME! │
# └──────────────────────────┘

# #Modulo 1
# from datetime import datetime
# import random

# print ('-------------------BEM VINDO A NOSSA EMPRESA----------------------')
# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# data_cadastro = datetime.now()
# cartoes = ['R$ 50,00', 'R$ 250,00', 'R$ 120,00']
# cartao = random.choice(cartoes)
# aniversario = datetime.strptime(input(
#     'Digite sua data de aniversario no formato dd/mm/aaaa: '), '%d/%m/%Y')

# # modulo 2
# print(f'Olá {nome}, seu registro foi concluido com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.')
# print(f'\n$$$$$ Parabens $$$$$\n\nHouve um sorteio e voce ganhou um cartão de compra no valor de {cartao}.')


# ┌───────────┐
# │ MODULO 03 │
# └───────────┘
# ┌──────────────────────────────────────────┐
# │ COMO RESOLVER PROBLEMAS COM CONDICIONAIS │
# └──────────────────────────────────────────┘
'''
5 PILARES DA PROGRAMAÇÃO
1 - VARIAVEIS
2 - CONTROLE DE FLUXO <---
3 - COLEÇÕES
4 - CLASSES
5 - FUNÇÕES
'''
# ┌─────────────────────────────────┐
# │ PRINCIPAIS OPERADORES NO PYTHON │
# └─────────────────────────────────┘
'''
# OPERADORES LÓGICOS
# OPERADORES BOLEANOS
# OPERADORES DE IGUALDADE
'''
# ┌─────────────────────────────────────────────┐
# │ LOGICA DE COMPARAÇÃO COM OPERADORES LÓGICOS │
# └─────────────────────────────────────────────┘

'''
()  PARENTESES
**  EXPOENTE
*   MULTIPLICAÇÃO
/   DIVISÃO
//  DIVISÃO POR INTEIROS
%   MODULUS
+-  ADIÇÃO/SUBTRAÇÃO
==, !=. >, <, >=, <=, IS, IS NOT, IN, NOT IN    - COMPARADORES LOGICOS, IDENTI-
                                                DADE, PERTENCIMENTO EM CONJUN-
                                                TOS
NOT - NOT NOOLEADO
AND - AND BOOLEANO
OR  - OR BOOLEANO
'''
# PORQUE QUEREMOS COMPARAR?
idade = 15
print(idade > 17)  # False
print(idade < 17)  # True
print(idade <= 17)  # True
print(idade >= 17)  # False
print(idade == 17)  # False
print(idade != 17)  # True

# COMPARAÇÃO ENTRE OUTROS TIPO
print(True == False)  # False
print('Rafael' == 'rafael')  # False o 'r' != 'R"
print('b' > 'a')  # True
print(5 == '5')  # False

print(type(5))  # class int
print(type('5'))  # class str


# ┌─────────────────────────────────────┐
# │ COMPARAÇÃO COM OPERADORES BOOLEANOS │
# └─────────────────────────────────────┘

# VAMOS PENSAR POR EXEMPLO NO SEGUINTE:
idade = 21
possui_convite = False
filho_do_dono = True

print((idade >= 21) and (possui_convite == True))
print(idade >= 21 or possui_convite == True)

# maior de 21 e possui convite ou seja filho do dono
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))

# outros exemplow:
maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
# voce so pode trabalhar aqui se for maior de idade e possuir CTPS
print((maior_de_idade == True) and (possui_carteira_de_trabalho == True))
print(maior_de_idade and possui_carteira_de_trabalho)

# queremos contratar pessoas que ainda não possuem um veículo próprio,
# mas ja possuem CTPS
print(esta_trabalhando_atualmente == False) and (
    possui_veiculo_proprio == False) and (possui_carteira_de_trabalho == True)
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)


print('──────────────────────────────────────────────────────────────────────')
# Desafio
possui_passaporte = False
Passagem_comprada = False
Menor_de_idade = False

# uma pessoa so pode viajar se possuir passaporte e tiver passagem comprada e
# não for menor de idade
possui_passaporte = True
Passagem_comprada = True
Menor_de_idade = False
print((possui_passaporte and Passagem_comprada) and not Menor_de_idade)

# uma pessoa so pode viajar se possuir passaporte ou tiver passagem comprada e
# não for menor de idade
possui_passaporte = True
Passagem_comprada = True
Menor_de_idade = False
print((possui_passaporte or Passagem_comprada) and not Menor_de_idade)

# uma pessoa so pode viajar se não possuir passaporte ou não tiver passagem comprada e
# não for menor de idade
possui_passaporte = True
Passagem_comprada = True
Menor_de_idade = False
print((not possui_passaporte or Passagem_comprada) and not Menor_de_idade)

# uma pessoa não pode viajar se não possuir passaporte ou não tiver passagem comprada e
# for menor de idade
possui_passaporte = False
Passagem_comprada = False
Menor_de_idade = True
print((not possui_passaporte or not Passagem_comprada) and Menor_de_idade)


# ┌──────────────────────────┐
# │  COMPARAÇÃO DE IGUALDADE │
# └──────────────────────────┘

print('──────────────────────────────────────────────────────────────────────')
a = 'Pithon'
b = 'Pithon'
print(a == b)  # compara o valor
print(a is b)  # compara a identidade

c = 10
d = 10
print(c == d)
print(c is d)

a = 'Python é demais! E ainda nem estamos no topo.'
b = 'Python é demais! E ainda nem estamos no topo.'
print(a == b)
print(a is b)

print('──────────────────────────────────────────────────────────────────────')

cor_preferida = None
print(cor_preferida is None)

cor_preferida = 'vermelho'
print(cor_preferida is None)


# ┌─────────────────────────┐
# │ CONVERTENDO ENTRE TIPOS │
# └─────────────────────────┘

# conversão de tipos

# idade = input('Qual a sua idade?')
# print(int(idade) > 18)

print(type(str(5)))

# receber valores decimais
# altura_da_parede = input('Qual a altura da parede?')
# print(float(altura_da_parede) > 2.10)

# tipos
int()
str()
float()
list()
tuple()
dict()


# ┌─────────────────────────────────────────────┐
# │ RESOLVENDO PROBLEMAS REAIS COM CONDICIONAIS │
# └─────────────────────────────────────────────┘
# ┌──────────────────┐
# │ IF - ELIF - ELSE │
# └──────────────────┘

trabalho_terminado = False

if trabalho_terminado == True:
    print('Vamos sair')
else:
    print('Não pode sair agora.')

print('──────────────────────────────────────────────────────────────────────')
numero_atrasos = 4
if numero_atrasos >= 3:
    print('Va para a diretoria')
elif numero_atrasos == 2:
    print('Essa e sua segunda falta')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta')

# print('──────────────────────────────────────────────────────────────────────')
# velocidade = int(input('qual a velocidade? '))
# if velocidade <= 50:
#     print('Não foi multado')
# elif velocidade >=51 and velocidade <=60:
#     print('Levou multa de 2 pontos')
# elif velocidade >=61 and velocidade <= 75:
#     print('Levou multa de 3 pontos')
# else:
#     print('Levou multa de 7 pontos')

# # Metodo Chaining:
# velocidade = int(input('qual a velocidade? '))
# if velocidade <= 50:
#     print('Não foi multado')
# elif 51 <=  velocidade <=60:
#     print('Levou multa de 2 pontos')
# elif 61 <= velocidade <= 75:
#     print('Levou multa de 3 pontos')
# else:
#     print('Levou multa de 7 pontos')
#
print('──────────────────────────────────────────────────────────────────────')

# DESAFIO:
tamanho_cabelo = 51
if tamanho_cabelo <= 20:
    print('Pagar R$ 50,00')
elif tamanho_cabelo >= 21 and tamanho_cabelo <= 30:
    print('Pagar R$ 70,00')
elif tamanho_cabelo >= 31 and tamanho_cabelo <= 50:
    print('Pagar R$ 100,00')
else:
    print('Favor consultar a receptção')


# ┌───────────────────┐
# │ OPERADOR TERNÁRIO │
# └───────────────────┘

idade = 15
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

print('──────────────────────────────────────────────────────────────────────')

idade = 30
print('Maior de idade') if idade >= 18 else print('Menor de idade')

print('──────────────────────────────────────────────────────────────────────')

possui_passaporte = True
print('Favor embarcar ') if possui_passaporte else print(
    'Favor tirar passaporte')

velocidade = 80
print('Voce foi multado') if velocidade > 100 else print('siga em frente')
print('──────────────────────────────────────────────────────────────────────')


# ┌─────────────────────┐
# │ LOOP FOR - LAÇO FOR │
# └─────────────────────┘

for numero in range(5):
    print('Carregando', numero)
print('──────────────────────────────────────────────────────────────────────')
for numero in range(1, 6):
    print('Carregando', numero)
print('──────────────────────────────────────────────────────────────────────')
for numero in range(1, 21, 2):
    print('Carregando', numero)
print('──────────────────────────────────────────────────────────────────────')
nomes = ['jeff', 'carl', 'jean', 'luke']
for nome in nomes:
    print(nome)
print('──────────────────────────────────────────────────────────────────────')

# Desafios:
for numero in range(18, 111):
    print('estamos em', numero)

for numero in range(1, 11):
    print('Realizando passo', numero)

# ┌────────────────────────────────┐
# │ NESTED LOOPS (LOOPS ANINHADOS) │
# └────────────────────────────────┘

#PAIS + ESTAÇÃO

paises = ['brasil', 'india', 'estados unidos']
estacoes_do_ano = ['primavera', 'verao', 'outono', 'inverno']
for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')

    for x in range(1, 10):
        for y in range(1, 6):
            print(f'Valor Externo {x} e interno {y}')
print('─────────────────────────────────────────────────────────────────────')
# DESAFIO
celulares = ['Asus', 'Samsung', 'Sony', 'Iphone']
versoes = ['plus', 'premium plus', 'premium deluxe', 'plus premium ultra']
for celular in celulares:
    for versao in versoes:
        print(f'{celular}, {versao}')
print('─────────────────────────────────────────────────────────────────────')


# ┌───────────────────────────┐
# │ ITERÁVEIS - O QUE É ISSO? │
# └───────────────────────────┘

for item in range(10):
    print(item)

for letra in 'programação':
    print(letra)

for item in [2, 3, 4, 5]:
    print(item)


# ┌─────────────────────────┐
# │ LOOP WHILE (LAÇO WHILE) │
# └─────────────────────────┘
import os # limpar o console
os.system('cls') or None #limpar o console

tentativas = 0
while tentativas <3:
    print('tente novamente')
    tentativas += 1


senha =''
while senha != '123':
    senha = input('Digite a senha: ')

print('bem vindo')

nome = ''
while nome =='':
    nome = input("Digite seu nome: ")

print (f'Bem vindo {nome}.')

horario = 0
while horario <= 17:
    print(horario)
    horario += 1
print (f'Hora de ir ver o por do sol {nome}!')

contador = 100 #contador decrescente
while contador >=0:
    print(contador)
    contador -=1

    
# ┌───────────────────────────────────────┐
# │ PASS - NÃO TA PRONTO NÃO TEM PROBLEMA │
# └───────────────────────────────────────┘

numero = 0
while numero < 5:
    pass

for numero in range (10):
    pass

#clicar CTRL+C no terminal para interromper o programa


# ┌──────────────────┐
# │ BREAK E CONTINUE │
# └──────────────────┘

#AULA 15
#teste











print('──────────────────────────────────────────────────────────────────────')

# ┌───────────────────────────────────────────────────────────────────────────┐
# │                                                                           │
# └───────────────────────────────────────────────────────────────────────────┘
# alt+218 = ┌
# alt+217 = ┘
# alt+192 = └
# alt+191 = ┐
# alt+179 = │
# alt+196 = ─

# (179) --> │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬
# ╧ ╨ ╤ ╥ ╙ ╒ ╒ ╓ ╫ ╪ ┘ ┌ █ ▄ ▐ ▀
# αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■

# ┌──────────────────────────────────────────────────────────────────┐
# │ATALHOS DO VSCODE                                                 │
# ├──────────────────────────────────────────────────────────────────┤
# │CTRL-K,C : COMENTAR CÓDIGO                                        │
# │CTRL-K,U : DESCOMENTAR CÓDIGO                                     │
# │ALT+SHIFT+SETA PRA CIMA/BAIXO : DUPLICA LINHA                     │
# │CTRL+B : HABILITAR/DESABILITAR BARRA LATERAL ESQUERDA             │
# │CTRL+' : HABILITAR DESABILITAR TERMINAL                           │
# │CTRL+F : BUSCAR PALAVRAS                                          │
# │CTRL+SHIFT+A : SUBSTITUIR TODAS AS OCORRENCIAS DE UMA PALAVRA     │
# │CTRL+P : NAVEGAR ATÉ UM ARQUIVO                                   │
# │CTRL+W : FECHAR JANELA                                            │
# │CTRL+(1,2,3,4) : NAVEGAR ENTRAR JANELAS ABERTAS NO VSCODE         │
# │F12 : NAVEGAR ATÉ O CÓDIGO FONTE                                  │
# │TAB: INDENTAÇÃO                                                   │
# │CTRL+C: NO TERMINAL: INTERROMPE A EXECUÇÃO DE LOOP                │
# │                                                                  │
# │                                                                  │
# └──────────────────────────────────────────────────────────────────┘


# 5 PILARES DA PROGRAMAÇÃO
# 1 - VARIAVEIS
# 2 - CONTROLE DE FLUXO
# 3 - COLEÇÕES
# 4 - CLASSES
# 5 - FUNÇÕES

#LIMPAR O CONSOLE
# import os 
# os.system('cls') or None 