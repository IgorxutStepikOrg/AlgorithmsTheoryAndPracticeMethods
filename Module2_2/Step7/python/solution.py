def fib_digit(num):

    if num == 0:
        return 0

    x, y, z = 0, 1, num + 1

    for i in range(2, z):
        x, y = y, (x + y) % 10

    return y


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
