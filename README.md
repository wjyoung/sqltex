Author: Will Young

## Description

The sqltex project reads a .sql file, runs the file using psql and returns a properly formatted Latex file, output.tex. Some edits will be necessary to finalize presentation. Some other functionality to be added including converting a .txt output file from psql to a .tex file without rerunning the queries in the background.

## Instructions

from the command line run:
python sqltex.py -d databasename -f filename.sql
