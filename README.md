# CS50 DNA Project

## Overview
The goal of the DNA Analysis project is to analyze a DNA sequence and determine the matching individual from a database of DNA profiles. The project simulates the basic principles of DNA profiling used in forensic analysis.

## Problem Description
In this project, you’ll work with a DNA database containing profiles of individuals. Each profile consists of a name and counts of consecutive short tandem repeats (STRs) found in their DNA. Your task is to write a program that:
1. Reads a DNA sequence.
2. Compares the sequence against the STR counts from a database.
3. Identifies which individual’s DNA matches the sequence.

### Input Files
- **CSV Database**: The CSV file contains a list of individuals along with the number of STR repeats for each STR type.
- **DNA Sequence**: A text file containing the DNA sequence that needs to be analyzed.

### Output
- The name of the individual whose DNA profile matches the given sequence.
- If no match is found, the program prints `No match`.

## STRs (Short Tandem Repeats)
STRs are short sequences of DNA that repeat consecutively. For example, the sequence `AGAT` might repeat twice in the sequence `AGATAGAT`. These STR counts are unique to individuals and can be used to identify them.

## Program Flow
1. **Load Data**: Read in the DNA sequence from the text file and the DNA database from the CSV file.
2. **STR Count**: Analyze the DNA sequence to count how many times each STR repeats consecutively.
3. **Match Profile**: Compare the STR counts with each profile in the database.
4. **Output**: Print the name of the matching individual, or `No match` if none of the profiles match.

## Installation
To run this project, you’ll need Python installed. You can clone this repository and run the program from the command line.

Clone this repository:
   ```bash
   git clone https://github.com/your-username/cs50-dna
   cd cs50-dna
