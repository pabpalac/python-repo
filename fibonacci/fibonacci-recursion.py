# Python program to display the Fibonacci sequence

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


def main():
    n_terms = int(input("¿Cuánros términos? "))

    # check if the number of terms is valid
    if n_terms <= 0:
        print("Por favor ingresa un número entero positivo.")
    else:
        print("Seguencia de Fibonacci:")
        for i in range(n_terms):
            print(recur_fibo(i))


main()
