#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


d = []
chps = []
for line in open("counts.tsv"):
    chapter, chunks, words = line.strip().split()
    book, chp = chapter.split(".")
    d.append((book, chapter, int(chunks), int(words)))
    chps.append(int(chp))

df = pd.DataFrame(d, columns=["book", "chapter", "chunks", "words"])

sns.set_style("whitegrid")
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
b1 = sns.barplot(y="chunks", x="chapter", hue="book", data=df, ax=ax1, dodge=False)
b2 = sns.barplot(y="words", x="chapter", hue="book", data=df, ax=ax2, dodge=False)

b1.legend_.remove()
b2.legend_.remove()

ax1.set_xlabel("")
ax1.set_xticklabels(chps)
ax2.set_xticklabels(chps)

f.suptitle("Chunk and Word Counts by Chapter in Lord of the Rings", y=0.95, weight='semibold')

f.text(0.01, 0.02, "Digital Tolkien Project • digitaltolkien.com", size='medium', color='black', weight='medium')
f.text(0.99, 0.02, "Little Delving #004", horizontalalignment='right', size='medium', color='black', weight='medium')

f.subplots_adjust(bottom=0.2)

plt.savefig("004.png")
