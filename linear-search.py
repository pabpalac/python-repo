from numpy.random import randint


def linear_search(values, element):
    index = 0
    for currentElement in values:
        if currentElement == element:
            return index
        index = index + 1
    return -1


def main():
    array_list = randint(0, 50, 50)
    result = linear_search(array_list, int(input("Ingresar número a la lista: \n")))
    if result > 0:
        print("Encontrado en la posición número " + str(result + 1))
    else:
        print("404 not found")
    print(array_list)


main()
