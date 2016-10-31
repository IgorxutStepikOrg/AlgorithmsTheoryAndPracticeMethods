def main():

    n, m = [int(i) for i in input().split()]
    lines, dct = list(), dict()

    for i in range(n):
        a, b = [int(i) for i in input().split()]
        lines.append([a, 0])  # левая граница отрезка
        lines.append([b, 2])  # правая граница отрезка

    points = [int(i) for i in input().split()]

    for i in points:
        lines.append([i, 1])  # точка на отрезке (может совпадать и с левой или правой границей отрезка)
        dct.update({i: 0})

    lines.sort(key=lambda x: [x[0], x[1]])

    counter = 0
    for i in lines:

        if i[1] == 0:
            counter += 1

        if i[1] == 1:
            dct[i[0]] = counter

        if i[1] == 2:
            counter -= 1

    for i in points:
        print(dct[i], end=" ")


if __name__ == "__main__":
    main()
