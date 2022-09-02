# linear-search.py: function to perform linear searching.
def linear_search(lista, x):
    i = 0
    for z in lista:
        if z == x:
            return i
        i = i + 1
    return -1


def main():
    print(linear_search([1, 4, 54, 3, 0, -1], 44))
    print(linear_search([1, 4, 54, 3, 0, -1], 3))
    print(linear_search([1, 4, 54, 3, 0, -1], 0))
    print(linear_search([], 0))


main()
