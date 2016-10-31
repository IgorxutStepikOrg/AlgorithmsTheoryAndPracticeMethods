def gcd(num1, num2):

    x, y = num1, num2

    while True:

        if x == 0:
            return y

        if y == 0:
            return x

        if x > y:
            x, y = x % y, y
        else:
            x, y = y % x, x


def main():

    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
