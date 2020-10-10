def even_fibonacci(even_num):
    even_list = [0]
    count_even = 1
    fib1, fib2 = 1, 1

    while count_even != even_num:
        fib1, fib2 = fib2, fib1 + fib2

        if fib2 % 2 == 0:
            count_even += 1
            even_list.append(fib2)

    print(even_list)
    return even_list


if __name__ == '__main__':
    err = False
    while not err:
        try:
            num = int(input("Количество четных элементов: "))
        except ValueError:
            print("Введено неверное значение. Введите заново.")
        else:
            err = True

    even_fibonacci(num)
