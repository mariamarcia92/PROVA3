numero_correto = 7  
tentativas_restantes = 3

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 3 tentativas para adivinhar o número correto, que está entre 1 e 10.\n")

while tentativas_restantes > 0:
    
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_correto:
        print("Parabéns! Você acertou o número!")
        break  
    else:
        tentativas_restantes -= 1  
        print(f"Errado! Você ainda tem {tentativas_restantes} tentativas.\n")
else:
   
    print("Que pena! Você usou todas as suas tentativas. O número correto era 7.")
    print("Não desista, tente novamente da próxima vez!")