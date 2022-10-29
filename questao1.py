import math

anos = int
meses = int
dias = int
idadedias = int(input('\nDigite a sua idade em dias: '))

anos = math.floor(idadedias / 365)
meses = math.floor((idadedias % 365) / 30)
dias = math.floor((idadedias % 365) % 30)

print(f'\nVoce tem {anos} anos, {meses} meses, e {dias} dias de idade.')