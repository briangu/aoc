import pandas

h = 0
d = 0
a = 0

df = pandas.read_csv('2.input',sep=' ')

for _,(cmd,x) in df.iterrows():
    if cmd == "forward":
        h += x
        d += a * x
    elif cmd == "down":
        a += x
    elif cmd == "up":
        a -= x

print(h,d,h*d)

