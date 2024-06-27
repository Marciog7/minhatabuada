while True:
    num = int(input("Digite um número para ver a sua tabuada: "))
    if num == -1:
        break
    for c in range(1, 11):
        print(f"{num} x {c:2} = {num*c}")
print("Fim da sua tabuada!")
