def main():

    n = int(input())
    A = [int(i) for i in input().split()]
    D = [0] * n

    for i in range(n):

        for j in range(i):

            if A[i] % A[j] == 0 and D[j] > D[i]:
                D[i] = D[j]

        D[i] += 1

    print(max(D))


if __name__ == "__main__":
    main()
