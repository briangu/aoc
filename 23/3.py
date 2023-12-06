import sys

def scan(m, i, j):
    """look for cells that are non-numeric and not dot '.' around cell i, j"""
    for y in range(j-1,j+2):
        for x in range(i-1,i+2):
            if m[y][x] != '.' and not m[y][x].isdigit():
                return True
    return False


def read_matrix(filename):
    a = []
    with open(filename) as f:
        for line in f:
            a.append('.'+line.strip()+'.')

    a.insert(0, '.'*len(a[0]))
    a.append('.'*len(a[0]))
    return a


def find_adjacent_numbers(m):
    """scan the matrix for digits that are adjacent to non-numeric cells"""
    digits = []
    for j in range(1,len(m)-1):
        d = ''
        adjacent = False
        for i in range(1,len(m[j])-1):
            if m[j][i].isdigit():
                adjacent = adjacent or scan(m, i, j)
                d += m[j][i]
            elif d:
                if adjacent:
                    digits.append(int(d))
                    adjacent = False
                d = ''
    return digits

m = read_matrix(sys.argv[1])
print(m)
digits = find_adjacent_numbers(m)
print(digits)
print(sum(digits))

