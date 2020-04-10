#!/bin/bash


sort_samples () {
  echo -n "$1" >> $FILENAME

  # Using O(n^2) algs
  ./bubble_sort.out $1 | tr -d '\n' >> $FILENAME
  ./insertion_sort.out $1 | tr -d '\n'  >> $FILENAME
  ./selection_sort.out $1 | tr -d '\n'  >> $FILENAME

  # Using O(n logn) algs
  ./heap_sort.out $1 | tr -d '\n'  >> $FILENAME
  ./merge_sort.out $1 | tr -d '\n'  >> $FILENAME
  ./quick_sort.out $1 | tr -d '\n'  >> $FILENAME

  echo "" >> $FILENAME
}


# Compile the latest version of sorting Algs
make


# Create output file
# e.g. results_20200220145755
curr_time=$(date +%Y%m%d%H%M%S)
FILENAME="results_$curr_time"
touch $FILENAME


lscpu >> $FILENAME

# Small to large input tests
for ((i = 16 ; i <= 262144 ; i = i * 2 )); do
  sort_samples $i
done

# "Largerer" input tests
for ((i = 262144 ; i <= 1048576 ; i = i += 262144 )); do
  sort_samples $i
done

make clean
