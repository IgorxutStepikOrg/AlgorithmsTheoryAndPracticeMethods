def knapsackwithoutrepsbu(weight, count, items):

    A = [0] * (weight + 1)
    B = [0] * (weight + 1)
    A[0] = 1

    for i in range(count):

        for j in range(weight, items[i] - 1, -1):

            if A[j - items[i]] == 1:
                A[j] = 1
                B[j] = items[i]

    k = weight

    while A[k] == 0:
        k -= 1

    return k


def main():

    W, n = map(int, input().split())
    gold = [int(i) for i in input().split()]

    print(knapsackwithoutrepsbu(W, n, gold))


if __name__ == "__main__":
    main()
