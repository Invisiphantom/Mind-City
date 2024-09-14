
import random
def RANDOMIZE_IN_PLACE(A):
    n = len(A)
    for i in range(n):
        j = random.randint(i, n-1)
        A[i], A[j] = A[j], A[i]
    return A


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(RANDOMIZE_IN_PLACE(A))