
import time
import numpy as np


def print_matrix(matrix: list[list]):
    for i in matrix:
        for j in i:
            print("%5d" % j, end=' ')
        print()


def count_zero(matrix: list[list]) -> int:
    count = 0
    for i in matrix:
        for j in i:
            if j == 0:
                count += 1
    return count


def get_sum_on_diagonal(matrix: list[list]) -> int:
    summa = 0
    for i in range(len(matrix)):
        summa += matrix[i][i] + matrix[i][len(matrix) - i - 1]

    return summa - matrix[len(matrix) // 2][len(matrix) // 2]


def main():
    while True:
        N = input("Введите N: ")
        if N.isdigit():
            N = int(N)
            break
        else:
            print("Введёт некорректный фотмат числа")
    while True:
        K = input("Введите K: ")
        if K.isdigit():
            K = int(K)
            break
        else:
            print("Введёт некорректный фотмат числа")

    N_over_two = N // 2

    A = np.random.randint(-10, 10, (N, N))
    print("Матрица А: ")
    print_matrix(A)

    E = [[A[i][j] for j in range(N_over_two)] for i in range(N_over_two)]
    print("Матрица E: ")
    print_matrix(E)

    B = [[A[i][j] for j in range(N_over_two, N)] for i in range(N_over_two)]
    print("Матрица B: ")
    print_matrix(B)

    D = [[A[i][j] for j in range(N_over_two)] for i in range(N_over_two, N)]
    print("Матрица D: ")
    print_matrix(D)

    C = [[A[i][j] for j in range(N_over_two, N)] for i in range(N_over_two, N)]
    print("Матрица C: ")
    print_matrix(C)

    A_t = np.transpose(A)
    print("Транспонированная матрица A: ")
    print_matrix(A_t)

    F = [[A[i][j] for j in range(N)] for i in range(N)]

    if count_zero(B) > count_zero(E):
        print("Нулей в B не меньше чем в E")
        for i in range(N_over_two):
            for j in range(N_over_two):
                F[i][j + N_over_two] = A[N - i - 1][j + N_over_two]
                F[i + N_over_two][j + N_over_two] = A[N_over_two - i - 1][j + N_over_two]
    else:
        print("Нулей в B меньше чем в E")
        for i in range(N_over_two):
            for j in range(N_over_two):
                F[i][j] = A[i][j + N_over_two]
                F[i][j + N_over_two] = A[i][j]

    print("Матрица F: ")
    print_matrix(F)

    if np.linalg.det(A) > get_sum_on_diagonal(F):
        print_matrix(np.dot(A, A_t) - K * np.array(F))
    else:
        print_matrix(K * (np.linalg.inv(A) + np.tril(A) - np.transpose(F)))


if __name__ == '__main__':
    start = time.time()
    main()
    print("\nProgram time: " + str(time.time() - start) + " seconds.")
