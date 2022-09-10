def get_row(row_index):
    cur_row = [1]
    if row_index == 0:
        return cur_row
    prev = get_row(row_index - 1)
    for i in range(1, len(prev)):
        curr = prev[i - 1] + prev[i]
        cur_row.append(curr)
    cur_row.append(1)
    return cur_row


def main():
    exponent = int(input("Introduce the binomial exponent: (a+b)^(?): "))
    pascal_row = get_row(exponent)
    pascal_row_length = len(pascal_row)
    a_exponent = pascal_row_length
    b_exponent = 1
    for i in range(pascal_row_length):
        a_exponent = a_exponent - i
        b_exponent = b_exponent + i
        current_item = pascal_row[i]
        if current_item == 1:
            if i < exponent / 2:
                print("a^" + str(exponent), end=" + ")
            else:
                print("b^" + str(exponent))
        else:
            print(str(pascal_row[i]) + "a^" + str(a_exponent) + "b^" + str(b_exponent), end=" + ")


main()
