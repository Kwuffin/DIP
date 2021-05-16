import sys
import numpy as np
import pandas as pd

all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "#", "%"]

df = pd.DataFrame(np.zeros((28, 28)), columns=all_letters, index=all_letters)

for line in sys.stdin:
    line.strip()

    word, count = line.split("\t")
    count = float(count.replace("\n", ""))

    l1, l2 = word.split("-")
    df.at[l1, l2] = count

total_count = df.to_numpy().sum()

for col in df:
    df[col] = df[col].apply(lambda x: x/total_count)

df.to_csv("OUT.csv")
