#!/usr/bin/env python3

from collections import Counter

word_counter = Counter()
para_counter = Counter()
books = set()

for line in open("../../texts/cite-index/lotr_para.txt"):
    ref, kind, text = line.strip().split("\t")
    words = text.replace("—", " ").split()
    book_ref = ref.split(".")[0]
    word_counter[book_ref] += len(words)
    para_counter[book_ref] += 1
    books.add(book_ref)


for book_ref in sorted(books):
    print(book_ref, para_counter[book_ref], word_counter[book_ref], sep="\t")
