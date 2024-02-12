def função_misteriosa(n):
    resultado = []
    for i in range(n):
        if i % 2 == 0:
            resultado.append(i * 2)
        else:
            resultado.insert(0, i)
    return resultado

print(função_misteriosa(5))