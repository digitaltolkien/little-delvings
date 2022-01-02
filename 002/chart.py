#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


adjustment = [
    100,
    100,
    100,
    0,
    100,
    100,
    100,
    100,
    100,
    200,
    100,
    100,
    100,
    100,
    100,
    100,
    -50,
    100,
    100,
]

d = []
for line in open("../001/counts.tsv"):
    chapter, chunks, words = line.strip().split()
    d.append((int(chapter), int(chunks), int(words)))

df = pd.DataFrame(d, columns=["chapter", "chunks", "words"])

plt.figure(figsize=(8, 8))
ax = sns.scatterplot(x="chunks", y="words", data=df, size=1, legend=False, color="black")

slope = sum(list(df.words)) / sum(list(df.chunks))
ax.plot([0, 160], [0, 160 * slope], "r--")

for idx in range(df.shape[0]):
    ax.text(df.chunks[idx] + 0.8, df.words[idx] - adjustment[idx], idx+1)
    # ax.text(df.chunks[idx], df.words[idx], idx+1, ha="center", va="center", size="medium")

ax.annotate("smaller chunks", xy=(90, 90 * slope), xytext=(90 + 15, (90 * slope) - (23 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")
ax.annotate("larger chunks", xy=(90, 90 * slope), xytext=(90 - 15, (90 * slope) + (23 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")

plt.title("Chunk and Word Counts by Chapter in the Hobbit", weight="semibold")

plt.text(-22, -1500, "Digital Tolkien Project • digitaltolkien.com", size="medium", color="black", weight="medium")
plt.text(178, -1500, "Little Delving #002", horizontalalignment="right", size="medium", color="black", weight="medium")

plt.xlim(0, 160)
plt.ylim(0, 12000)
plt.savefig("002.png")
