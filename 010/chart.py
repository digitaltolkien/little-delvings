#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

xlim = 150

chps = []
d = []
for line in open("../009/counts.tsv"):
    ref, chunks, words = line.strip().split()
    d.append((ref, int(chunks), int(words)))
    if ref.startswith("01."):
        chps.append("A")
    elif ref.startswith("02."):
        chps.append("VQ")
    elif ref.startswith("03."):
        chps.append(int(ref[3:]))
    elif ref.startswith("04."):
        chps.append("AK")
    elif ref.startswith("05."):
        chps.append("RP")
    else:
        assert False

x_adjustments = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    -4,
    1,
    1,
    1,
    1,
    1,
    1,
    -4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
y_adjustments = [
    -200,
    -200,
    100,
    -200,
    -200,
    -300,
    -200,
    -300,
    0,
    -200,
    -200,
    -300,
    -200,
    200,
    -200,
    -200,
    -200,
    -200,
    -200,
    -300,
    -200,
    100,
    -200,
    -200,
    -300,
    -200,
    -200,
    -200,
]
df = pd.DataFrame(d, columns=["chapter", "chunks", "words"])

plt.figure(figsize=(8, 8))
ax = sns.scatterplot(x="chunks", y="words", data=df, size=1, legend=False, color="black")

slope = sum(list(df.words)) / sum(list(df.chunks))
ax.plot([0, xlim], [0, xlim * slope], "r--")

for idx in range(df.shape[0]):
    ax.text(df.chunks[idx] + x_adjustments[idx], df.words[idx] + y_adjustments[idx], chps[idx], size="small")
    # ax.text(df.chunks[idx], df.words[idx], idx+1, ha="center", va="center", size="medium")

ax.annotate("smaller chunks", xy=(100, 100 * slope), xytext=(100 + 15, (100 * slope) - (15 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")
ax.annotate("larger chunks", xy=(100, 100 * slope), xytext=(100 - 15, (100 * slope) + (15 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")

plt.title("Chunk and Word Counts by Chapter in the Silmarillion", weight="semibold")

plt.text(-20, -2000, "Digital Tolkien Project • digitaltolkien.com", size="medium", color="black", weight="medium")
plt.text(165, -2000, "Little Delving #010", horizontalalignment="right", size="medium", color="black", weight="medium")

plt.xlim(0, xlim)
plt.ylim(0, xlim * slope)
plt.savefig("010.png")
