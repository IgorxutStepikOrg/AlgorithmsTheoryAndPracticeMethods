import numpy


def fib(num):

    matrix1 = numpy.array([0, 1])
    matrix2 = numpy.array([[0, 1], [1, 1]])
    matrix3 = numpy.linalg.matrix_power(matrix2, num)
    matrix4 = numpy.dot(matrix1, matrix3)

    return matrix4[0]


def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
