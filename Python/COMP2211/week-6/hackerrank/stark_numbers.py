def findTerm(n, c, a, b, m):
 
    def mat_mult(A, B):
        return [
            [
                (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % m,
                (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % m
            ],
            [
                (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % m,
                (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % m
            ]
        ]


    def mat_pow(mat, power):
        result = [[1, 0], [0, 1]]  # Identity matrix
        while power > 0:
            if power % 2 == 1:
                result = mat_mult(result, mat)
            mat = mat_mult(mat, mat)
            power //= 2
        return result

    # Transformation matrix
    T = [[a, b], [0, 1]]

    # Compute T^n
    Tn = mat_pow(T, n)

    # Multiply by initial vector [c, 1]
    xn = (Tn[0][0] * c + Tn[0][1]) % m

    return xn