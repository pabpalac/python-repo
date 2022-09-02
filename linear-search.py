# linear-search.py: function to perform linear searching.
def linear_search(values, element):
    index = 0
    for currentElement in values:
        if currentElement == element:
            return index
        index = index + 1
    return -1


def main():
    print(linear_search([1, 4, 54, 3, 0, -1], 44))
    print(linear_search([1, 4, 54, 3, 0, -1], 3))
    print(linear_search([1, 4, 54, 3, 0, -1], 0))
    print(linear_search([], 0))


main()
