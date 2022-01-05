#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

xlim = 300

chps = []
d = []
for line in open("../004/counts.tsv"):
    ref, chunks, words = line.strip().split()
    d.append((ref, int(chunks), int(words)))
    chps.append(ref)

df = pd.DataFrame(d, columns=["chapter", "chunks", "words"])

plt.figure(figsize=(8, 8))
ax = sns.scatterplot(x="chunks", y="words", data=df, size=1, legend=False, color="black")

slope = sum(list(df.words)) / sum(list(df.chunks))
ax.plot([0, xlim], [0, xlim * slope], "r--")

for idx in range(df.shape[0]):
    ax.text(df.chunks[idx] + 2, df.words[idx], chps[idx], size="small")
    # ax.text(df.chunks[idx], df.words[idx], idx+1, ha="center", va="center", size="medium")

ax.annotate("smaller chunks", xy=(250, 250 * slope), xytext=(250 + 15, (250 * slope) - (15 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")
ax.annotate("larger chunks", xy=(250, 250 * slope), xytext=(250 - 15, (250 * slope) + (15 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")

plt.title("Chunk and Word Counts by Chapter in Lord of the Rings", weight="semibold")

plt.text(-40, -2000, "Digital Tolkien Project • digitaltolkien.com", size="medium", color="black", weight="medium")
plt.text(330, -2000, "Little Delving #005", horizontalalignment="right", size="medium", color="black", weight="medium")

plt.xlim(0, xlim)
plt.ylim(0, xlim * slope)
plt.savefig("005.png")
