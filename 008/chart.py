#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

xlim = 2000

books = []
d = []
for line in open("../007/counts.tsv"):
    ref, chunks, words = line.strip().split()
    d.append((int(ref), int(chunks), int(words)))
    books.append(int(ref))

df = pd.DataFrame(d, columns=["book", "chunks", "words"])

plt.figure(figsize=(8, 8))
ax = sns.scatterplot(x="chunks", y="words", data=df, legend=False, color="black")

slope = sum(list(df.words)) / sum(list(df.chunks))
ax.plot([0, xlim], [0, xlim * slope], "r--")

for idx in range(df.shape[0]):
    ax.text(df.chunks[idx] + 20, df.words[idx] - 1000 - books[idx] * 200, books[idx], size="medium")
    # ax.text(df.chunks[idx], df.words[idx], idx+1, ha="center", va="center", size="medium")

ax.annotate("smaller chunks", xy=(1300, 1300 * slope), xytext=(1300 + 150, (1300 * slope) - (150 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")
ax.annotate("larger chunks", xy=(1300, 1300 * slope), xytext=(1300 - 150, (1300 * slope) + (150 * slope)),
            arrowprops=dict(color="blue", arrowstyle="<-"), ha="center", va="center", color="blue")

plt.title("Chunk and Word Counts by Book in Lord of the Rings", weight="semibold")

plt.text(-250, -12000, "Digital Tolkien Project • digitaltolkien.com", size="medium", color="black", weight="medium")
plt.text(2200, -12000, "Little Delving #008", horizontalalignment="right", size="medium", color="black", weight="medium")

plt.xlim(0, xlim)
plt.ylim(0, xlim * slope)
plt.savefig("008.png")
