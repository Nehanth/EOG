#!/usr/bin/env Rscript
setwd("/Users/srilokh/Projects/EOG/Data")
args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==1) {
  # default output file
  library(readr)
  fileName <- args[1]
  rawData <- read_csv(toString(fileName))
  cleanData <- rawData[rowSums(is.na(rawData)) == 0,]
  cleanData <- cleanData[cleanData$BIT_DEPTH >= 0,]
  cleanFileName <- gsub(" ", "",paste("/Users/srilokh/Projects/EOG/Data/","clean", fileName))
  print(paste("Creating dataset", cleanFileName))
  write.csv(cleanData, cleanFileName, row.names=FALSE)
}

