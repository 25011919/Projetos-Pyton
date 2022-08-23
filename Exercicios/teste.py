# Receber dois numeros, e falar qual deles é par e qual deles é impar

primeiro_numero = int(input("Digite o primeiro numero:"))
segundo_numero = int(input("Digite o segundo numero:"))

def verifica_par_impar(numero):
    tipo = "par"
    if numero % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
    return tipo

tipo_primeiro_numero = verifica_par_impar(primeiro_numero)
tipo_segundo_numero = verifica_par_impar(segundo_numero)

print(f"O seu primeiro numero é: {tipo_primeiro_numero} e o seu segundo numero é: {tipo_segundo_numero}")
