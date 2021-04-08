entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0

    for x in range(3):
        # print(entradas[x])
        # print(pesos[x])

        s += e[x] * p[x]

    return s

s = soma(entradas, pesos)

print(s)


def stepFuncion(soma):
    if soma > 1:
        return 1
    return 0

r = stepFuncion(s)

print(r)