primeironum = int(input('\nDigite o primeiro número: '))
segundonum = int(input('\nDigite o segundo número: '))
terceironum = int(input('\nDigite o terceiro número: '))

menornum = primeironum

if (segundonum < menornum):
    menornum = segundonum
if (terceironum < menornum):
    menornum = terceironum

print(f'\nO menor número digitado por você foi: {menornum}')