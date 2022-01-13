#!/bin/sh

(cd ../009; ./count.py > counts.tsv)
./chart.py
