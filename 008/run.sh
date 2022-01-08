#!/bin/sh

(cd ../007; ./count.py > counts.tsv)
./chart.py
