#!/bin/bash

chess_samples_python () {
  echo -n "$1 " >> $FILENAME_PYTHON
  echo -n "$2 " >> $FILENAME_PYTHON

  # Python implementation
  { time { python3 play_vs_self.py $1 $2 &> /dev/null ; } } 2>> $FILENAME_PYTHON
}

# For the bash builtin time, set the TIMEFORMAT
TIMEFORMAT=%R

# Create output file
# e.g. nqueens_results_20200220145755
curr_time=$(date +%Y%m%d%H%M%S)
FILENAME_PYTHON="PYTHON_chess_results_$curr_time"

# Create files
touch $FILENAME_PYTHON

lscpu >> $FILENAME_PYTHON

# Input tests for Python
for ((i = 10 ; i <= 100 ; i = i + 5 )); do
  for ((j = 10 ; j <= 100 ; j = j + 5 )); do
    chess_samples_python $i $j
  done
done


make clean
