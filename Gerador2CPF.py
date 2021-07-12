from random import randint


def gerar_cpf():
    cpf = str(randint(100000000, 999999999))
    x = confirme = 0
    y = 10

    for digito in range(2):
        soma = 0

        for var in cpf:
            soma += int(var) * y
            y -= 1
        confirme = 11 - (soma % 11)

        if x == 0:
            if int(confirme) > 9:
                confirme = '0'
            cpf += str(confirme)

        if x == 1:
            cpf += str(confirme)

        x += 1
        y = 11
    return cpf


print(gerar_cpf())