import reader
import re


doc_template = """\\documentclass[12 pt]{article}
\\usepackage[margin = 1 in]{geometry}
\\usepackage{amsmath, amsthm, amssymb, amsfonts, listings, textcomp, booktabs, color, lscape, wrapfig}
\\geometry{left = 0.5 in, right = 0.5 in, footskip = 0.25 in}
\\begin{document}
\\title{INSERT TITLE}
\\author{INSERT AUTHORS}
\\maketitle
\\begin{flushleft}
%s
\\end{flushleft}
\\end{document}
"""

query_template = """\\begin{verbatim}%s;
\\end{verbatim}
"""

table_template = """\\begin{table}[h]
\\scriptsize
\\centering
\\caption{INSERT CAPTION}
\\label{my - label}
\\begin{tabular}{%s}
\\hline
%s\\hline
\\end{tabular}
\\end{table}
\\pagebreak
"""


def build_body(data):
    """
    Builds Latex formatted string for queries and tables from sql file.

    :param data: string representation of psql queries and tables
    :return: Latex formatted string of the queries and tables
    """
    s = ""
    for i, datum in enumerate(data):
        if i % 2 == 0:  # adding the SQL command
            s += query_template % datum
        else:  # adding the SQL output (table)
            s += build_table(datum)
    return s


def build_table(line):
    """
    Takes a psql formatted table and returns a Latex formatted table.

    :param line: string representation of a psql formatted table
    :return: Latex formatted table
    """
    return table_template % (get_column_marker(line), parse_csv(line))


def build_tex_string(data):
    """
    Creates a Latex formatted string from psql output.

    :param data: A string representation of psql output (queries and tables).
    :return: A Latex typesettable formatted string.
    """
    data = reader.read_sql(data)
    return doc_template % build_body(data)


def get_column_marker(line):
    """
    Creates a string of 'c's to set the number of columns in LAtex document.

    :param line: string of psql output
    :return: string of c's
    """
    line = line.lstrip('\n')
    line = line.splitlines()[0]
    num_cols = line.count(',') + 1
    return 'c ' * num_cols


def parse_csv(csv_str):
    """
    Converts a csv into a Latex table. Does not include preambles for the table just its body.

    :param csv_str: a string representation of a csv table
    :return: Latex formatted table body
    """
    l = csv_str.split(',')
    s = ' & '.join(l)
    s = re.sub('\\n', '\\\\\\\n', s)
    return s


def write_tex_file(data):
    """
    Writes data to output.tex in local directory.

    :param data: a string
    :return: None
    """
    s = build_tex_string(data)
    fd = open("output.tex", "w")
    fd.write(s)
    fd.close()
