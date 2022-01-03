#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

d = []

for line in open("../../texts/cite-index/hobb_para.txt"):
    ref, kind, text = line.strip().split("\t")
    chapter = ref.split(".")[0]
    words = text.replace("—", " ").split()
    if kind in ["{p}", "{ps}"]:
        d.append((ref, chapter, kind, len(words)))
    if len(words) > 300:
        print(ref)

df = pd.DataFrame(d, columns=["ref", "chapter", "kind", "Words per Paragraph"])

sns.set_style("ticks")

ax = sns.displot(df, x="Words per Paragraph", binwidth=10)

plt.title("Distribution of Words per Paragraph in the Hobbit", weight="semibold")

plt.text(-110, -45, "Digital Tolkien Project • digitaltolkien.com", size="medium", color="black", weight="medium")
plt.text(590, -45, "Little Delving #003", horizontalalignment="right", size="medium", color="black", weight="medium")

plt.subplots_adjust(left=0.15, bottom=0.2, right=0.85, top=0.9)

plt.savefig("003.png")
