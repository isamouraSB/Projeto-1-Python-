#aprendendo comandos do zero #4 (06/03/2023) 
 print("olá mundo")
print(7+4)
print ("7"+"4")
print("qual sua profissao","5")
nome = 'Isadora' # nome-variavel, (=)recebe 
idade = 25
peso = 75.8
print(nome,idade,peso)
nome = input('Qual o seu nome?')
idade = input('Quantos anos você tem?')
peso = input("Quanto você pesa?")
print(nome,idade,peso)

#exercicio 1 (script que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado )
nome = input("Qual o seu nome?")
print("Olá",nome,"! Prazer em te conhecer!")

#exercicio 2(script que leia o dia,o mês e ano de nascimento e mostra uma mensagem com a data formatada)
dia = input("Qual o dia do seu nascimento? ")
mes = input("Qual o mês?")
ano = input("E o ano do seu nascimento?")
print("Você nasceu no dia", dia,"de",mes,"de",ano,". Correto?")

#exercicio 3
valor1 = int(input("Primeiro numero: "))
valor2 = int(input("Segundo número: "))
reslt = (valor1+valor2)
print("A soma é:",reslt)