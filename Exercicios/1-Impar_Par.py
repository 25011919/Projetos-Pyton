#numero = int(input("Me diga um número? ") )
#resultado = numero % 2
#if resultado == 0:
   # print ("o numero {} é Par".format(número))
#else:
   # print("o número {} é ímpar".format(número))
    
#from curses.ascii import isdigit


numero_inteiro = input('Digite um numero inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    
    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par ')
    else:
        print(f'{numero_inteiro} é ímpar')
else:
    print('Isso não é um número inteiro ')        
    