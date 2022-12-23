
pairs = [
    [[1,1,3,1,1],[1,1,5,1,1]],
    [[[1],[2,3,4]],[[1],4]],
    [[9],[[8,7,6]]],
    [[[4,4],4,4],[[4,4],4,4,4]],
    [[7,7,7,7],[7,7,7]],
    [[],[3]],
    [[[[]]],[[]]],
    [[1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]],
    # [[[8,[[7]]]],[[[[8]]]]],
    # [[[8,[[7]]]],[[[[8],2]]]],
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


from functools import total_ordering
@total_ordering
class Wrapper:
    def __init__(self, x):
        self.x = x
    def __eq__(self,o):
        return compare(self.x, o.x) is None
    def __ne__(self,o):
        return not self.__eq__(o.x)
    def __lt__(self, o):
        return compare(self.x, o.x)
    # def __len__(self):
    #     return len(self.x)

packets = []
for p in pairs:
    packets.append(Wrapper(p[0]))
    packets.append(Wrapper(p[1]))
packets.append(Wrapper([[6]]))
packets.append(Wrapper([[2]]))

print(packets)
packets.sort()
# packets = sorted(packets)

product = 1
for i,r in enumerate(packets):
    if r.x == [[6]] or r.x == [[2]]:
        product *= i+1
    print(r.x)

print(product)
