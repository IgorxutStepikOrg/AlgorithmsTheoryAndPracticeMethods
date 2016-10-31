def fib_mod(num1, num2):

    lst = [0, 1]
    counter = 0

    if num1 > (num2 ** 2 + 1):
        k = num1
    else:
        k = num1 ** 2 + 1

    for i in range(2, k):
        counter += 1
        lst.append((lst[i - 1] + lst[i - 2]) % num2)

        if lst[i] == 1 and lst[i - 1] == 0:
            break

    return lst[num1 % counter]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
