#!/bin/sh

(cd ../004; ./count.py > counts.tsv)
./chart.py
