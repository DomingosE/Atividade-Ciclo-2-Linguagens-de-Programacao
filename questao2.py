import math
while True:

        LadoA = int(input('\nDigite o valor do lado "A" do triângulo: '))
        LadoB = int(input('\nDigite o valor do lado "B" do triângulo: '))
        LadoC = int(input('\nDigite o valor do lado "C" do triângulo: '))

        if LadoA <= 0 or LadoB <= 0 or LadoC <= 0:

            print('\nFavor digitar apenas valores positivos, ou seja, valores superiores ao número 0')

        else:
            break

ValorTotal = (LadoA+LadoB+LadoC)

if LadoA >= (LadoB+LadoC) or LadoB >= (LadoA+LadoC) or LadoC >= (LadoA+LadoB):
    print(f'\nSe somarmos os valores do lado "A" = {LadoA}, lado "B" = {LadoB}, e lado "C" = {LadoC} temos o valor total de {ValorTotal}. Esse valor total não forma um triângulo.')

else:
    perimetro = (LadoA+LadoB+LadoC)/2
    area = math.sqrt(perimetro*(perimetro-LadoA)*(perimetro-LadoB)*(perimetro-LadoC))
    print(f'\nA área de todo o triângulo é: {area:.2f}')
