preço = float(input("Qual é o valor do produto? R$"))
novo = preço - (preço * 15 / 100)
print("O produto que custava R${:.2f},  com o desconto de 15% vai custar R${:.2f}".format(preço, novo))

preço = float(input("Qual é o valor do produto? R$"))
novo = preço - (preço * 10 / 100)
print("O produto que custava R${:.2f},  com o desconto de 10% vai custar R${:.2f}".format(preço, novo))

preço = float(input("Qual é o valor do produto? R$"))
novo = preço - (preço + 10 / 100)
print("O produto que custava R${:.2f},  com o desconto de 10% vai custar R${:.2f}".format(preço, novo))
