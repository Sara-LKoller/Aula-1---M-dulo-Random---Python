import random

print("Advinhe!")

n_secreto = random.randint(1,100)

while True:
    chute = int(input("Chute um número de 0 a 100: "))

    if chute == n_secreto:
        print("Acertou!")
        break
    elif chute < n_secreto:
        print("Valor menor, chute um número mais ALTO")
    else:
        print("Valor maior, chute um número mais BAIXO")
