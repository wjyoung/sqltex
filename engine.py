import reader
import re


query_template = """\\begin{verbatim}%s;
\\end{verbatim}
"""

preamble = """\\documentclass[12 pt]{article}
\\usepackage[margin = 1 in]{geometry}
\\usepackage{amsmath, amsthm, amssymb, amsfonts, listings, textcomp, booktabs, color, lscape, wrapfig}
\\geometry{left = 0.5 in, right = 0.5 in, footskip = 0.25 in}
\\begin{document}
\\title{INSERT TITLE}
\\author{INSERT AUTHORS}
\\maketitle
\\begin{flushleft}
"""

postamble = """\end{flushleft}
\end{document}
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


def build_preamble():
    """
    Returns the boilerplate header for a Latex file.

    :return: Latex header string
    """
    return preamble


def build_postamble():
    """
    Returns the boilerplate footer for a Latex file.

    :return: Latex footer string
    """
    return postamble


def build_table(line):
    """
    Takes a psql formatted table and returns a Latex formatted table.

    :param line: string representation of a psql formatted table
    :return: Latex formatted table
    """
    s = line
    if s[0] == '\n':
        s = s[1:]
    s = s[:s.find('\n')-1]
    num_cols = s.count(',') + 1
    col_marker = 'c ' * num_cols
    s = table_template % (col_marker, parse_csv(line))
    return s


def build_tex_string(data):
    """
    Creates a Latex formatted string from psql output.

    :param data: A string representation of psql output (queries and tables).
    :return: A Latex typesettable formatted string.
    """
    data = reader.read_sql(data)
    s = build_preamble()
    s += build_body(data)
    s += build_postamble()
    return s


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
