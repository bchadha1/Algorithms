def ThreeStringLCS(X, Y, Z, m, n, o):
    Length = [[[0 for i in range(o + 1)] for j in range(n + 1)] for k in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if j == 0 or k == 0 or i == 0:
                    Length[i][j][k] = 0

                elif X[i - 1] == Z[k - 1] and X[i - 1] == Y[j - 1]:
                    Length[i][j][k] = Length[i - 1][j - 1][k - 1] + 1

                else:
                    Length[i][j][k] = max(max(Length[i - 1][j][k], Length[i][j - 1][k]), Length[i][j][k - 1])

    return Length[m][n][o]

    # LCS_Array = [""] * (Length[m][n][o] + 1)
    # LCS_Array[Length[a][b][o]] = ""

    LCS_Array = ""
    while m > 0 and l > 0 and n > 0:
        step = subs[m][n][o]
        if step == subs[m - 1][n][o]:
            m = m - 1
        elif step == subs[m][n - 1][o]:
            n = n - 1
        elif step == subs[m][n][o - 1]:
            o = o - 1
        else:
            LCS_Array = LCS_Array + str(X[m - 1])
            m = m - 1
            n = n - 1
            o = o - 1

    return LCS_Array[::-1]

    print("Longest Common Subsequence (LCS) of the three strings is : ", LCS_Array)


X = '6541254939322816220209974565477289648317'
Y = '3142522751761601737419090933147067701840'
Z = '2807030561290354259513570160162463275171'

# m = len(X)
# n = len(Y)
# o = len(Z)

print('Length of LCS is', ThreeStringLCS(X, Y, Z, len(X), len(Y), len(Z)))