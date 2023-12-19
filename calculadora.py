import time

print ('\n1- Soma\n2- Multlicação\n3- Divisão\n4- Potencia')
escolha = int(input('escolha a operação que será feita: '))
num1 = float(input('Digite o primeiro numero:'))
num2 = float(input('Digite o segundo numero:'))

if escolha == 1: 
    print(f'= {num1 + num2}')
elif escolha == 2:
    print(f'= {num1 * num2}')
elif escolha == 3:
    print(f'= {num1 // num2}')
elif escolha == 4:
    print(f'= {num1 ** num2}')
else:
    print('Esolha uma opção valida!')

    time.sleep(20)