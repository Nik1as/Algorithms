import random


def fisher_yates_shuffle(A):
    n = len(A)
    for i in range(n - 1):
        j = random.randint(i, n - 1)
        A[i], A[j] = A[j], A[i]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fisher_yates_shuffle(A)
    print(A)
