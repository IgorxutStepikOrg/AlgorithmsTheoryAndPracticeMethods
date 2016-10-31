from heapq import heappush, heappop


def main():

    n = int(input())
    lst, heap = list(), list()

    for i in range(n):

        lst.append(input().split())

        if lst[i][0] == "Insert":
            heappush(heap, -int(lst[i][1]))

        if lst[i][0] == "ExtractMax":
            print(-heappop(heap))


if __name__ == "__main__":
    main()
