import pandas as pd

df = pd.read_csv('3.input', dtype={'bin': str})
q = df.apply(lambda r: pd.Series([int(z) for z in r['bin']]), axis=1)
m = q.mean()

g = 0
e = 0

for i,x in enumerate(m):
    b = 1 if x > 0.5 else 0
    z = 2 ** (len(m)-i-1)
    print(x, b, i, z)
    g += b * z
    b = 0 if b == 1 else 1
    e += b * z

print(g,e,g*e)

