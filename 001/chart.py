#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


d = []
for line in open("counts.tsv"):
    chapter, chunks, words = line.strip().split()
    d.append((int(chapter), int(chunks), int(words)))

df = pd.DataFrame(d, columns=["chapter", "chunks", "words"])

sns.set_style("whitegrid")
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5))
sns.barplot(y="chunks", x="chapter", data=df, ax=ax1)
sns.barplot(y="words", x="chapter", data=df, ax=ax2)

ax1.set_xlabel("")
f.suptitle("Chunk and Word Counts by Chapter in the Hobbit", y=0.95, weight='semibold')

f.text(0.01, 0.02, "Digital Tolkien Project • digitaltolkien.com", size='medium', color='black', weight='medium')
f.text(0.99, 0.02, "Little Delving #001", horizontalalignment='right', size='medium', color='black', weight='medium')

f.subplots_adjust(bottom=0.2)

plt.savefig("001.png")
