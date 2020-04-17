#!/bin/bash


matrix_samples () {
  echo -n "$1" >> $FILENAME

  # Using Loop-ordering cache friendly
  /usr/bin/time --verbose ./n3_sample2.out $1 >> $FILENAME
  echo "" >> $FILENAME

  # Using Strassen Algorithm
  /usr/bin/time --verbose ./n28074_sample1.out $1  >> $FILENAME
  echo "" >> $FILENAME
}


# Compile the latest version of matrix multiplication Algs
make


# Create output file
# e.g. results_20200220145755
curr_time=$(date +%Y%m%d%H%M%S)
FILENAME="results_$curr_time"
touch $FILENAME


lscpu >> $FILENAME

# Small samples tests
matrix_samples 16
matrix_samples 32
matrix_samples 48

# Larger input tests
for ((i = 64 ; i <= 2048 ; i = i + 64 )); do
  matrix_samples $i
done


make clean
