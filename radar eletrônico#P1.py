#projeto 1 CTD: Radar eletrônico

velocidade = float(input("Qual a velocidade atual do carro? "))#determinar a velocidade do carro
if velocidade > 80: #se a velocidade for maior que 80 exibir uma multa
    print("MULTADO! Você excedeu o limite permitido que é de 80km/h") #mensagem que o individuo recebe a multa
    multa = (velocidade-80) * 7 #  a multa =(igual) a velocidade -(menos) 80(que é a km permitida) *(vezes) o valor por km/h= 7
    print("Você deve pagar uma multa de R${:.2f}!".format(multa)) # o resultado é formatado com dois pontos decimais flutuantes
print("Tenha um bom dia! Dirija com segurança!")
        