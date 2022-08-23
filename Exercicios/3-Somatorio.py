def soma_dois_numeros(x,y):
    return x + y

def soma_numeros(*args):
    soma = 0
    for numero in args:
        soma = soma + numero 
    return soma
resultado_da_soma = soma_dois_numeros(1,2)
print(resultado_da_soma)
soma_varios_num = soma_numeros(1,2,3,4,5)
print(soma_varios_num)    