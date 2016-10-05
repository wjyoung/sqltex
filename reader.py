import sys
import re

def get_args():
    """
    Reads args provided and reacts accordingly.
    Not fully functional.

    :return: tuple containing database name and sql file name
    """
    db = None
    file_in = None
    if len(sys.argv) <= 2:
        file_in = get_data()
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-d':
            db = sys.argv[2]
            print "Enter .sql to run:"
            file_in = sys.stdin()
        else:
            sys.stderr.write("ERROR: Command not recognized %s" % sys.argv[1])
    elif len(sys.argv) == 5:
        if sys.argv[1] == sys.argv[3]:
            sys.stderr.write("ERROR: Command repeated")
            return db, file_in
        for i in [1, 3]:
            if sys.argv[i] == '-d':
                db = sys.argv[i + 1]
            elif sys.argv[i] == '-f':
                file_in = sys.argv[i + 1]
            else:
                sys.stderr.write("ERROR: Command not recognized %s" % sys.argv[1])
    else:
        sys.stderr("Unsupported number of arguments given")
    return db, file_in


def get_data():
    """
    Reads the file provided by arg[1] or stdin if no arg given.

    :return: A string of the contents of the file
    """
    if len(sys.argv) == 1:  # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data  # or data.strip?


def read_sql(data):
    """
    Read sql with queries from data string and return a list of lines

    :return: A formatted string of the sql queries and tables
    """
    #data = data.strip('\r')
    data = re.sub('\\(\\d* \\w*\\)', ";", data)
    data = re.sub('&', '\&', data)
    data = re.sub('_', '\_', data)
    data = re.sub('%', '\%', data)
    data = data.split(';')
    return data
