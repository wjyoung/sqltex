import reader
import re


def build_body(data):
    s = ""
    for i in range(len(data)):
        if i % 2 == 0:  # adding the SQL command
            s += "\\begin{verbatim}" + data[i] + "; \n \\end{verbatim} \n"
        else:  # adding the SQL output (table)
            s += build_table(data[i])
    return s


def build_preamble():
    s = "\\documentclass[12 pt]{article} \n " \
             "\\usepackage[margin = 1 in]{geometry} \n " \
             "\\usepackage{amsmath, amsthm, amssymb, amsfonts, listings, textcomp, booktabs, color, lscape, wrapfig} \n" \
             "\\geometry{left = 0.5 in, right = 0.5 in, footskip = 0.25 in} \n" \
             "\\begin{document} \n" \
             "\\title{INSERT TITLE} \n" \
             "\\author{INSERT AUTHORS} \n" \
             "\\maketitle \n" \
             "\\begin{flushleft}"
    return s


def build_postamble():
    s = "\end{flushleft}" \
        "\end{document} \n"
    return s


def build_table(line):
    s = "\\begin{table}[h] \n" \
             "\\scriptsize \n" \
             "\\centering \n" \
             "\\caption{INSERT CAPTION} \n" \
             "\\label{my - label} \n" \
             "\\begin{tabular}{" + 'c ' * 12 + "}" + parse_csv(line) + "\\end{tabular} \n \\end{table} "
    return s


def build_tex_string(data):
    data = reader.read_sql(data)
    s = build_preamble()
    s += build_body(data)
    s += build_postamble()
    return s


def parse_csv(csv_str):
    l = csv_str.split(',')
    s = ' & '.join(l)
    s = re.sub('\\n', '\\\\\\\n', s)
    return s


def write_tex_file(data):
    s = build_tex_string(data)
    fd = open("output.tex", "w")
    fd.write(s)
    fd.close()
