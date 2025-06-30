print('hello world!')
print('Esse é meu primeiro scrpt')
print('estou aprendendo Python') #printa texto na tela
print(1+2) #soma
print(1-2) #subtrai 
print(5 ** 2) #eleva 5 ao quadrado
type (5.5) #mostra o tipo de dado
type(5)
print("textos em python") 
print(type('teste Lara'))
print(type('500'))
print(type(int('500'))) #transforma texto em numero
str(500) #transforma numero em texto
print(50+10) #soma de numeros
print('teste'+'lara') #concatena texto
print('teste' + ' ' + 'lara') #concatena texto com espaço
print('lara' * 3) #repete texto pelo numero de vezes da multiplicação 

len("lara")#conta o tamanho do texto
print(len("lara")) #conta o tamanho do texto e printa nao aceita para numero 
print(type("lara")) #mostra o tipo de dado
#int é numero inteiro, float é numero decimal, str é texto

help(print) #mostra a ajuda do comando print
print('teste', 'lara', sep='-') #separa os textos com o caracter
print('teste', 'lara', sep='-', end='!') #separa os textos com o caracter e termina com o caracter

###################
#variaveis 
print(3.14*5**2) #calculo da area do circulo
pi=3.14 #variavel pi
raio=5 #variavel raio  
area=pi*raio**2 #variavel area
print(area) #printa a area do circulo

##regras de nomeação de variaveis
#1- Não pode começar com numero 
#2- Não pode conter espaços
#3- Não pode conter caracteres especiais (exceto _)
#4- Não pode ser uma palavra reservada do python (ex: print, if, else, etc)
#5- Não pode conter acentos
#6 - Não pode ser muito longo
#7 - diferenciar maiusculas de minusculas (ex: nome e Nome são diferentes)
#8 - Não pode ser igual a outra variavel

##############

x = input()
print(x)  # printa o valor da variavel x
##quando se uso o input com aspas é possivel criar um prmpt para o usuario digitar algo no terminal
# Exemplo de uso do input
input("digite um numero: ")  # pede para o usuario digitar um numero
x = input("digite um numero: ")  # pede para o usuario digitar um
print("o numero digitado foi: " + x)  #printa o numero digitado pelo usuario


x = input("digite um numero: ")  # pede para o usuario digitar um numero
x_num = int(x)  # converte o valor digitado para inteiro
print(x_num + 10) #se nao converter antes de somar, o python entende que é uma string e nao soma

x =int(input("digite um numero: ") ) # pede para o usuario digitar um numero
print(x + 10)  # soma 10 ao numero digitado pelo usuario


#desafio
# crie um programa que:
# pede seu nome e idade
#dá oi para voce
#conta quantas letras seu nome possui
#fala quandos anos voce terá em 5 anos


#pega os inputs do usuario
nome = input("Qual é o seu nome? ")  # pede o nome do usuario
idade = int(input("Qual é a sua idade? "))  # pede a idade do usuario
#resposta do desafio 
print("Olá, " + nome + "!")  # dá oi para o usuario
print("Seu nome tem " + str(len(nome)) + " letras.")  # conta quant
print("Em 5 anos, você terá " + str(idade + 5) + " anos.")  # fala quantos anos o usuario terá em 5 anos. tem que converter o numero em string para poder concatenar com o texto
print("Olá, " + nome + "! " + "Seu nome tem " + str(len(nome)) + " letras." + " Em 5 anos, você terá " + str(idade + 5) + " anos.")  # dá oi para o usuario

