#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


d = []
books = []
for line in open("counts.tsv"):
    book, chunks, words = line.strip().split()
    d.append((book, int(chunks), int(words)))
    books.append(int(book))

df = pd.DataFrame(d, columns=["book", "chunks", "words"])

sns.set_style("whitegrid")
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
b1 = sns.barplot(y="chunks", x="book", hue="book", data=df, ax=ax1, dodge=False)
b2 = sns.barplot(y="words", x="book", hue="book", data=df, ax=ax2, dodge=False)

b1.legend_.remove()
b2.legend_.remove()

ax1.set_xlabel("")
ax1.set_xticklabels(books)
ax2.set_xticklabels(books)

f.suptitle("Chunk and Word Counts by Book in Lord of the Rings", y=0.95, weight='semibold')

f.text(0.02, 0.02, "Digital Tolkien Project • digitaltolkien.com", size='medium', color='black', weight='medium')
f.text(0.98, 0.02, "Little Delving #007", horizontalalignment='right', size='medium', color='black', weight='medium')

# f.subplots_adjust(bottom=0.2)

plt.savefig("007.png")
