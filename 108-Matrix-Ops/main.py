# Matrix Operations
def print_matrix(m, name=""):
    if name: print(f"\n{name}:")
    for row in m:
        print("  " + " ".join(f"{x:4d}" for x in row))

def add_matrices(a, b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")
print_matrix(add_matrices(A, B), "A + B")
print_matrix(transpose(A), "Transpose of A")
