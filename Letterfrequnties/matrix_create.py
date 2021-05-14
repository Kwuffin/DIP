import sys
import numpy as np
import pandas as pd

all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "#", "%"]

df = pd.DataFrame(np.zeros((28, 28)), columns=all_letters, index=all_letters)
print(df)

for line in sys.stdin:
    line.strip()

    word, count = line.split("\t")
    count = int(count.replace("\n", ""))


