import pandas

df = pandas.read_csv("1.input", header=None)
df = df.rolling(3).sum()
df = df.dropna()
df = df.diff()
print(len(df[df[0] > 0]))



