def countsort(nums):

    M = max(nums) + 1
    B = [0] * M
    C = list()

    for i in nums:
        B[i] += 1

    for j in range(M):
        C += [j] * B[j]

    return C


def main():

    n = int(input())
    A = [int(i) for i in input().split()]

    print(" ".join(map(str, countsort(A))))


if __name__ == "__main__":
    main()
