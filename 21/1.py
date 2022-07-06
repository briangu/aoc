import pandas

df = pandas.read_csv("1.input", header=None)
df = df.diff()
print(len(df[df[0] > 0]))



