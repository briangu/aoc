import pandas

h = 0
d = 0

df = pandas.read_csv('2.input',sep=' ')

for _,(cmd,x) in df.iterrows():
    if cmd == "forward":
        h += x
    elif cmd == "down":
        d += x
    elif cmd == "up":
        d -= x

print(h,d,h*d)
