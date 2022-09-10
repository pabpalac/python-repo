def obtener_fila_piramide_pascal(indice_de_fila):
    esta_fila = [1]
    if indice_de_fila == 0:
        return esta_fila
    anterior = obtener_fila_piramide_pascal(indice_de_fila - 1)
    for i in range(1, len(anterior)):
        esta_fila.append(anterior[i - 1] + anterior[i])
    esta_fila.append(1)
    return esta_fila


def principal():
    exponente = int(input("Introduce the binomial exponent: (a+b)^(?): "))
    fila_pascal = obtener_fila_piramide_pascal(exponente)
    tamanio_fila_pascal = len(fila_pascal)
    exponente_a = tamanio_fila_pascal - 2
    exponente_b = 1
    for i in range(tamanio_fila_pascal):
        este_valor = fila_pascal[i]
        if este_valor == 1:
            if i < exponente / 2:
                print("a^" + str(exponente), end=" + ")
            else:
                print("b^" + str(exponente))
        else:
            print(este_valor, end="")
            if exponente_a == 1:
                print("a", end="")
            else:
                print("a^" + str(exponente_a), end="")
            if exponente_b == 1:
                print("b", end=" + ")
            else:
                print("b^" + str(exponente_b), end=" + ")
            exponente_a = exponente_a - 1
            exponente_b = exponente_b + 1


principal()
