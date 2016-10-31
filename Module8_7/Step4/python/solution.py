def main():

    n = int(input())
    a = [int(i) for i in input().split()]
    a.insert(0, 0)

    b = a[:2]
    for i in a[2:]:
        b = (b[1], max(b) + i)

    print(b[1])


if __name__ == "__main__":
    main()
