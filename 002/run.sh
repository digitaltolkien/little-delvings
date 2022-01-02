#!/bin/sh

(cd ../001; ./count.py > counts.tsv)
./chart.py
