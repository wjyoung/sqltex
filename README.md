Author: Will Young

## Description

The sqltex project reads a .sql file, runs the file using psql and returns a properly formatted Latex file, output.tex. Some edits will be necessary to finalize presentation. Some other functionality to be added including converting a .txt output file from psql to a .tex file without rerunning the queries in the background.

## Instructions

from the command line run:
python sqltex.py -d databasename -f filename.sql

The .sql file should be formatted as:
 
 -- comment of some sort
 
 -- do not include a semicolon in the comments. The only
 
 -- place for a semi colon is at the end of a query.
 
 --  There must be a semicolon at the end of the query.
 
 -- It is a good idea to use limits otherwise Latex is overloaded.
 
 SELECT col_1
 
 FROM table_A
 
 LIMIT 10;