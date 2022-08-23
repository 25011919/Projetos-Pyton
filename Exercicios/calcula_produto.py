forma_de_pagamento = int(input(
    "Escolha a forma de pagamento\n"
    "1 - Dinheiro\n"
    "2 - Credito\n"
    "3 - Parcelado\n"
))
valor_etiqueta_produto = 94.00
preco_final = 0

# formas de pagamento
dinheiro = 1
credito = 2
parcelado = 3

DESCONTO_DINHEIRO= 0.85
DESCONTO_CREDITO= 0.90
JUROS_PARCELADO= 1.10


def calcula_valor_final_parcelado(numero_parcelas):
    if numero_parcelas == 2:
        preco_final = valor_etiqueta_produto
    else:
        preco_final = valor_etiqueta_produto * JUROS_PARCELADO
    return preco_final

if forma_de_pagamento == dinheiro:
    preco_final = valor_etiqueta_produto * DESCONTO_DINHEIRO
elif forma_de_pagamento == credito:
    preco_final = valor_etiqueta_produto * DESCONTO_CREDITO
elif forma_de_pagamento == parcelado:
    numero_parcelas = int(input("Quantas parcelas?\n"))
    preco_final = calcula_valor_final_parcelado(numero_parcelas)


print(f"O valor final do produto será: {preco_final:.2f}")