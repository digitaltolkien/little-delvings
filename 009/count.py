#!/usr/bin/env python3

from collections import Counter

word_counter = Counter()
para_counter = Counter()
chapters = set()

for line in open("../../texts/cite-index/silm_para.txt"):
    ref, kind, text = line.strip().split("\t")
    words = text.replace("—", " ").split()
    chapter_ref = ".".join(ref.split(".")[:2])
    word_counter[chapter_ref] += len(words)
    para_counter[chapter_ref] += 1
    chapters.add(chapter_ref)


for chapter_ref in sorted(chapters):
    print(chapter_ref, para_counter[chapter_ref], word_counter[chapter_ref], sep="\t")
