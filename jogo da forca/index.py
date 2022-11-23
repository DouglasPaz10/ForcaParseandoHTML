import finding

tentativas = 0
chances = 8

letras_escolhidas = []
palavra_secreta = finding.palavra.upper()
estado_atual = ["_"] * len(palavra_secreta)

print(finding.dica1)
while tentativas < chances and ''.join(estado_atual) != palavra_secreta:

	letra = input("\n\nQual letra você quer tentar? ").upper()

	while letra in letras_escolhidas:
		print ("Você escolheu uma letra que já tinha tentado, escolha outra")
		letra = input("\nQual letra você quer tentar? ")

	letras_escolhidas.append(letra)

	if letra in palavra_secreta:
		print ("Parabéns, você acertou a letra!\n \n")
		for i in range(len(palavra_secreta)):
			if letra == palavra_secreta[i]:
				estado_atual[i] = letra
	else:
		print ("Que pena, você errou!")
		tentativas = tentativas + 1


	print ("Você já fez", tentativas, "tentativas erradas e ainda tem", chances-tentativas, "tentativas" )


	print ("Esse é o estado atual:")
	print (estado_atual)


	print ("As letras que você já tentou são:")
	for item in letras_escolhidas:
		print (item, end=" ")


if tentativas == chances:
	print ("\n\nVocê perdeu")
	print ("Acabaram suas tentativas")
else:
	print ("\n\nVocê ganhou, parabéns")

print ("A palavra era", palavra_secreta)









