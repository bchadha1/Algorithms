README

The python file SimplexMethod.py takes the values of coefficients of 3 linear equations in the form of an array and retuns the result of the linear programming problem using the Simplex Algorithm.
The program also takes the slack variables for all the equations.

The program outputs a pivot matrix after each step.

----------------------------------------------------------------------------

INPUT

c = [20, 10, 15]
A = [[3, 2, 5], [2, 1, 1], [1, 1, 3], [5, 2, 4]]
b = [55, 26, 30, 57]

#slack variables
A[0] += [1, 0, 0, 0]
A[1] += [0, 1, 0, 0]
A[2] += [0, 0, 1, 0]
A[3] += [0, 0, 0, 1]
c += [0, 0, 0, 0]

-----------------------------------------------------------------------------

OUTPUT

Initial matrix:
[3, 2, 5, 1, 0, 0, 0, 55]
[2, 1, 1, 0, 1, 0, 0, 26]
[1, 1, 3, 0, 0, 1, 0, 30]
[5, 2, 4, 0, 0, 0, 1, 57]
[20, 10, 15, 0, 0, 0, 0, 0]

Next pivot index is=1,1 

Matrix after pivot:
[-1.0, 0.0, 3.0, 1.0, -2.0, 0.0, 0.0, 3.0]
[2.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 26.0]
[-1.0, 0.0, 2.0, 0.0, -1.0, 1.0, 0.0, 4.0]
[1.0, 0.0, 2.0, 0.0, -2.0, 0.0, 1.0, 5.0]
[0.0, 0.0, 5.0, 0.0, -10.0, 0.0, 0.0, -260.0]

Next pivot index is=0,2 

Matrix after pivot:
[-0.3333333333333333, 0.0, 1.0, 0.3333333333333333, -0.6666666666666666, 0.0, 0.0, 1.0]
[2.3333333333333335, 1.0, 0.0, -0.3333333333333333, 1.6666666666666665, 0.0, 0.0, 25.0]
[-0.33333333333333337, 0.0, 0.0, -0.6666666666666666, 0.33333333333333326, 1.0, 0.0, 2.0]
[1.6666666666666665, 0.0, 0.0, -0.6666666666666666, -0.6666666666666667, 0.0, 1.0, 3.0]
[1.6666666666666665, 0.0, 0.0, -1.6666666666666665, -6.666666666666667, 0.0, 0.0, -265.0]

Next pivot index is=3,0 

Matrix after pivot:
[0.0, 0.0, 1.0, 0.19999999999999998, -0.8, 0.0, 0.2, 1.6]
[0.0, 1.0, 0.0, 0.6000000000000001, 2.6, 0.0, -1.4000000000000004, 20.799999999999997]
[0.0, 0.0, 0.0, -0.8, 0.19999999999999987, 1.0, 0.20000000000000004, 2.6]
[1.0, 0.0, 0.0, -0.4, -0.4000000000000001, 0.0, 0.6000000000000001, 1.8000000000000003]
[0.0, 0.0, 0.0, -0.9999999999999999, -6.0, 0.0, -1.0, -268.0]

[(0, 1.8000000000000003), (1, 20.799999999999997), (2, 1.6), (5, 2.6)]
268.0



-------------------------------------------------------------------------



SOURCE CODE

import heapq

def col(A, j):
    row_j = [row[j] for row in A]
    return row_j


def Trans(A):
    len_A = len(A[0])
    range_len_A = range (len_A)
    col_A_j = [col(A, j) for j in range_len_A]
    return col_A_j


def Std_form(cost, greaterThans=[], gtThreshold=[], lessThans=[], ltThreshold=[],
         equalities=[], eqThreshold=[], maximization=True):
    newVars = 0
    numRows = 0
    if ltThreshold:
        newVars = newVars + len(ltThreshold)
        numRows = numRows + len(ltThreshold)
    if eqThreshold:
        numRows = numRows + len(eqThreshold)
    if gtThreshold:
        newVars = newVars + len(gtThreshold)
        numRows = numRows + len(gtThreshold)

    if maximization == 0:
        cost = [-x for x in cost]

    if newVars == 0:
        return cost, equalities, eqThreshold

    newCost = list(cost) + [0] * newVars

    constraints = []
    threshold = []

    oldConstraints = [(greaterThans, gtThreshold, -1), (lessThans, ltThreshold, 1),
                      (equalities, eqThreshold, 0)]

    offset = 0
    for constraintList, oldThreshold, coefficient in oldConstraints:
        constraints += [c + r for c, r in zip(constraintList,
                                              Id(numRows, newVars, coefficient, offset))]

        threshold += oldThreshold
        offset += len(oldThreshold)

    return newCost, constraints, threshold


def dot_prod(a, b):
    sum = sum(x * y for x, y in zip(a, b))
    return sum


def Improve(matrix):
    lastRow = matrix[-1]
    return any(x > 0 for x in lastRow[:-1])


def more_Than_1_Min(L):
    len_L = len(L)
    if len_L <= 1:
        return False

    heapq_n_smallest = heapq.nsmallest(2, L, key=lambda x: x[1])
    x, y = heapq_n_smallest
    return x == y


def Pivot_Col(col):
    L = len([c for c in col if c == 0])
    len_col = len(col)
    return (L == len_col - 1) and sum(col) == 1


def init_Table(c, A, b):
    matrix = [row[:] + [x] for row, x in zip(A, b)]
    matrix.append([ci for ci in c] + [0])
    return matrix


def primal_Soln(matrix):
    # the pivot columns denote which variables are used
    columns = Trans(matrix)
    indices = [j for j, col in enumerate(columns[:-1]) if Pivot_Col(col)]
    return [(colIndex, Var_val_pivot_col(matrix, columns[colIndex]))
            for colIndex in indices]


def Id(numRows, numCols, val=1, rowStart=0, i=None):
    R = range(numCols)
    Id_val = [(val if i == j else 0) for j in R for i in range(rowStart, numRows)]
    return Id_val


def objective_Val(matrix):
    obj_val = abs(matrix[-1][-1])
    return obj_val


def Var_val_pivot_col(matrix, column):
    pivotRow = [i for (i, x) in enumerate(column) if x == 1][0]
    return matrix[pivotRow][-1]


def simplex_algo(c, A, b):
    matrix = init_Table(c, A, b)
    print("Initial matrix:")
    for row in matrix:
        print(row)
    print()

    while Improve(matrix):
        pivot = pivot_index(matrix)
        print("Next pivot index is=%d,%d \n" % pivot)
        Abt_pivot(matrix, pivot)
        print("Matrix after pivot:")
        for row in matrix:
            print(row)
        print()

    return matrix, primal_Soln(matrix), objective_Val(matrix)


def Abt_pivot(matrix, pivot):
    i, j = pivot

    pivot_d = matrix[i][j]
    matrix[i] = [x / pivot_d for x in matrix[i]]

    for k, row in enumerate(matrix):
        if k != i:

            pivotRowMultiple = [y * matrix[k][j] for y in matrix[i]]
            zip_matrix = zip(matrix[k], pivotRowMultiple)
            matrix[k] = [x - y for x, y in zip_matrix]


def pivot_index(matrix):
    column = min(((i, x) for (i, x) in enumerate(matrix[-1][:-1]) if x > 0), key=lambda a: a[1])[0]

    if all(row[column] <= 0 for row in matrix):
        raise Exception('Linear program is unbounded.')

    # check for degeneracy: more than one minimizer of the quotient
    quotients = [(i, r[-1] / r[column])
                 for i, r in enumerate(matrix[:-1]) if r[column] > 0]

    if more_Than_1_Min(quotients):
        raise Exception('Linear program is degenerate.')

    # pick row index minimizing the quotient
    row = min(quotients, key=lambda x: x[1])[0]

    return row, column


c = [20, 10, 15]
A = [[3, 2, 5], [2, 1, 1], [1, 1, 3], [5, 2, 4]]
b = [55, 26, 30, 57]

A[0] += [1, 0, 0, 0]
A[1] += [0, 1, 0, 0]
A[2] += [0, 0, 1, 0]
A[3] += [0, 0, 0, 1]
c += [0, 0, 0, 0]

t, s, v = simplex_algo(c, A, b)
print(s)
print(v)