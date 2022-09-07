# Python program to display the Fibonacci sequence

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


def main():
    n_terms = int(input("How many terms? "))

    # check if the number of terms is valid
    if n_terms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(n_terms):
            print(recur_fibo(i))


main()
