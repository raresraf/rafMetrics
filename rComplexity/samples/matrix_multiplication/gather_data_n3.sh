#!/bin/bash

make clean
make

curr_time=$(date +%Y%m%d%H%M%S)

FILENAME="results_$curr_time"
touch $FILENAME

for ((i = 64 ; i <= 10000 ; i*=2)); do
  echo "$i" >> $FILENAME
  ./n3_sample0.out $i >> $FILENAME
  ./n3_sample1.out $i >> $FILENAME
  ./n3_sample2.out $i >> $FILENAME
  ./n3_sample3.out $i >> $FILENAME
done