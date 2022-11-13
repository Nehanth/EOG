#!/bin/bash
for file in /Users/srilokh/Projects/EOG/Data/Asteroid*.csv
do
  echo 'cleaning ' $file
  sudo Rscript --vanilla /Users/srilokh/Projects/EOG/Data/clean.R $file 
done
