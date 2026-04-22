excelente = 0
ruim = 0
for quantidade in range(1, 11):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade: "))
    opiniao = input("Qual sua opinião do atendimento prestado: \n 1- Excelente \n 2- Bom \n 3- Ruim \n")
    if opiniao == "1":
        excelente = excelente + 1
    elif opiniao == "3":
        ruim = ruim + 1
print("Quantidade de pessoas que responderam excelente: ", excelente)
print("Quantidade de pessoas que responderam ruim: ", ruim)