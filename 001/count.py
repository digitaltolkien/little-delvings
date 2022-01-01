#!/usr/bin/env python3

from collections import Counter

word_counter = Counter()
para_counter = Counter()

for line in open("../../texts/cite-index/hobb_para.txt"):
    ref, kind, text = line.strip().split("\t")
    words = text.replace("—", " ").split()
    chapter_num, para_num = ref.split(".")
    word_counter[int(chapter_num)] += len(words)
    para_counter[int(chapter_num)] += 1

for chapter_num in range(1, 20):
    print(chapter_num, para_counter[chapter_num], word_counter[chapter_num], sep="\t")
