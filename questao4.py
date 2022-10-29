while True:

        numerointeiro = int(input('\nDigite um número inteiro entre 1 e 100: '))

        if numerointeiro <= 0 or numerointeiro > 100:

            print('\nFavor digitar apenas valores positivos entre 1 e 100!')

        else:
            break

def VerificaNumero(num):

    totalnum = 0

    for cont in range(1, num+1):
        if num % cont == 0:
            totalnum += 1

    if totalnum == 2:

        print('\nO valor digitado por você é um número primo, ou seja, ele possui apenas dois divisores. O número 1 e ele mesmo.\n')
        return True

    else:
        print('\nO valor digitado por você não é um número primo, ou seja, ele pode ser dividido por mais de dois números.\n')
        return False

print(VerificaNumero(numerointeiro))