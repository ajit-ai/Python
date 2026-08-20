def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def fibonacci_iterative(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def fibonacci_matrix(n):
    def mat_mult(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def mat_pow(M, p):
        result = [[1, 0], [0, 1]]
        while p:
            if p % 2 == 1:
                result = mat_mult(result, M)
            M = mat_mult(M, M)
            p //= 2
        return result

    if n <= 0:
        return []
    if n == 1:
        return [0]
    M = [[1, 1], [1, 0]]
    seq = [0, 1]
    for i in range(2, n):
        result_mat = mat_pow(M, i - 1)
        seq.append(result_mat[0][0])
    return seq
