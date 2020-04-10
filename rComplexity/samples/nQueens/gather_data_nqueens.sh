#!/bin/bash


nqueens_samples_c () {
  echo -n "$1 " >> $FILENAME_C

  # C implementation
  { time { ./nqueens.out $1 &> /dev/null ; } } 2>> $FILENAME_C
}

nqueens_samples_python () {
  echo -n "$1 " >> $FILENAME_PYTHON

  # Python implementation
  { time { python3 nqueens.py $1 &> /dev/null ; } } 2>> $FILENAME_PYTHON
}


# Compile the latest version of Algs
make

# For the bash builtin time, set the TIMEFORMAT
TIMEFORMAT=%R

# Create output file
# e.g. nqueens_results_20200220145755
curr_time=$(date +%Y%m%d%H%M%S)
FILENAME_C="C_nqueens_results_$curr_time"
FILENAME_PYTHON="PYTHON_nqueens_results_$curr_time"

# Create files
touch $FILENAME_C
touch $FILENAME_PYTHON

lscpu >> $FILENAME_C
lscpu >> $FILENAME_PYTHON

# Input tests for C
for ((i = 1 ; i <= 18 ; i = i + 1 )); do
  nqueens_samples_c $i
done

# Input tests for Python
for ((i = 1 ; i <= 16 ; i = i + 1 )); do
  nqueens_samples_python $i
done


make clean
