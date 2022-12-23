
pairs = [
    [[1,1,3,1,1],[1,1,5,1,1]],
    [[[1],[2,3,4]],[[1],4]],
    [[9],[[8,7,6]]],
    [[[4,4],4,4],[[4,4],4,4,4]],
    [[7,7,7,7],[7,7,7]],
    [[],[3]],
    [[[[]]],[[]]],
    [[1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]],
    [[[8,[[7]]]],[[[[8]]]]],
    [[[8,[[7]]]],[[[[8],2]]]],
]

if True:
    pairs = []
    with open("13.raw", "r") as f:
        arr = f.readlines()
        for i in range(0, len(arr), 3):
            print(i)
            s = arr[i].strip()
            print(s)
            a = eval(s)
            s = arr[i+1].strip()
            print(s)
            b = eval(s)
            print(f"{a},{b}")
            pairs.append([a,b])


def compare(a,b):
    print(f"compare: {a} {b}")
    i,j = 0,0
    while i < len(a) and j < len(b):
        if isinstance(a[i],int) and isinstance(b[j],int):
            if a[i] < b[j]:
                print(f"{a[i]} < {b[i]}")
                return True
            elif a[i] > b[j]:
                print(f"{a[i]} > {b[i]}")
                return False
            else:
                i += 1
                j += 1
                continue
        aa = [a[i]] if isinstance(a[i],int) else a[i]
        bb = [b[j]] if isinstance(b[j],int) else b[j]
        sub_compare = compare(aa,bb)
        print(f"sub_compare: {sub_compare} {aa} {bb}")
        if sub_compare:
            return True
        if sub_compare is None:
            i += 1
            j += 1
            continue
        return False
    if len(a) < len(b):
        return True
    if len(a) > len(b):
        return False
    return None


results = []
for p in pairs:
    a = p[0]
    b = p[1]
    print()
    r = compare(a,b)
    print(f"*** {a} {b} {r}")
    results.append((f"*** {a} {b} {r}",r))

print()
s = 0
for i,r in enumerate(results):
    print(r)
    if r[1]:
        s += 1+i

print(s)


