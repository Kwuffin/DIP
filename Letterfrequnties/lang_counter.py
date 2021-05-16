import pandas as pd
import numpy as np
import sys

all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "#", "%"]

# Pre-trained matrices
df_nl = pd.read_csv("NL.csv", index_col=0)
df_en = pd.read_csv("EN.csv", index_col=0)

for line in sys.stdin:
    df = pd.DataFrame(np.zeros((28, 28)), columns=all_letters, index=all_letters)
    line.strip()

    word, count = line.split("\t")
    count = float(count.replace("\n", ""))

    l1, l2 = word.split("-")

    # Set value of specific point in DataFrame
    df.at[l1, l2] = count

    total_count = df.to_numpy().sum()

    # Divide by total amount of combinations to get a percentage
    for col in df:
        df[col] = df[col].apply(lambda x: x/total_count)

    # Calculate the differences between pre-trained matrices and input
    nl_diff_score = 0
    en_diff_score = 0

    df_nl_diff = pd.DataFrame(np.zeros((28, 28)), columns=all_letters, index=all_letters)
    df_en_diff = pd.DataFrame(np.zeros((28, 28)), columns=all_letters, index=all_letters)

    # Calculate differences between pre-trained matrices and input matrix.
    for col in range(len(df_nl)):
        for i in range(len(df_nl.iloc[0])):
            nl_diff_score += (int(df.iat[i, col]) - int(df_nl.iat[i, col]))

    for col in range(len(df_en)):
        for i in range(len(df_en.iloc[0])):
            en_diff_score += (int(df.iat[i, col]) - int(df_en.iat[i, col]))

    nl_diff_score = abs(nl_diff_score)
    en_diff_score = abs(en_diff_score)

    if nl_diff_score < en_diff_score:
        print("en\t1")

    elif en_diff_score < nl_diff_score:
        print("nl\t1")

    else:
        print("en\t1")

