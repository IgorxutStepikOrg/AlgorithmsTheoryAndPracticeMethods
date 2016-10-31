def fib(num):

    prev, cur = 0, 1

    for i in range(1, num):
        prev, cur = cur, prev + cur

    return cur


def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
