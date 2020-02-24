#!/bin/bash


matrix_samples () {
  echo -n "$1" >> $FILENAME
  ./n3_sample0.out $1 | tr -d '\n' >> $FILENAME
  ./n3_sample1.out $1 | tr -d '\n'  >> $FILENAME
  ./n3_sample2.out $1 | tr -d '\n'  >> $FILENAME
  ./n3_sample3.out $1 | tr -d '\n'  >> $FILENAME
  echo "" >> $FILENAME
}


# Compile the latest version of matrix multiplication Algs
make


# Create output file
# e.g. results_20200220145755
curr_time=$(date +%Y%m%d%H%M%S)
FILENAME="results_$curr_time"
touch $FILENAME


# Small samples tests
matrix_samples 32
matrix_samples 64
matrix_samples 128

# Larger input tests
for ((i = 256 ; i <= 4096 ; i = i + 256 )); do
  matrix_samples $i
done


make clean