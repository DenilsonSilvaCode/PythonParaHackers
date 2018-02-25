#Recursão == quando você tem uma função chamando a si propria

# 2 ** 4 == 2 * 2 * 2 * 2

def pot(b, e):       #criando função para potenciação
    if e == 0:
        return 1
    else:
        return b * pot(b, e - 1)

print(pot(2, 0))
