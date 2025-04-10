print ("Olá, seja bem vindo!")
nome = input ("Qual seu nome? ")

print (f"Ok {nome}, vamos te retornar a soma de dois numeros!")
numero1 = int(input ("Digite um numero: "))
print (f"Isso {nome}, vamos prosseguir!")
numero2 = int(input ("Digite outro numero: "))
soma = numero1 + numero2
print (f"O seu resultado é: {soma}")


print (f"Ok {nome}! o que quer fazer agora, Divisao ou Multiplicaçao?")
escolha = input ("Digite sua resposta: ")

if escolha == "multiplicacao": 
    print (f"Ok {nome}")
    numero1 = int(input ("Digite um numero: "))
    numero2 = int(input ("Digite outro numero: "))
    multiplicacao = numero1 * numero2
    print (f"Seu resultado é: {multiplicacao}")

if escolha == "divisao": 
    print (f"Ok, {nome}! vamos lá: ")
    escolha = input ("Sao numeros inteiros ou reais? ")
    if escolha == "inteiros":
        numero1 = int(input ("Digite um numero: "))
        numero2 = int(input ("Digite outro numero: "))
        resultado = numero1 // numero2 
        print (f"Legal, {nome}! O seu resultado é: {resultado}")
    elif escolha == "reais":
        numero1 = float(input ("Digite um numero: "))
        numero2 = float(input ("Digite outro numero: "))
        resultado = numero1 / numero2
        print (f"Legal, {nome}! O seu resultado é: {resultado}")
