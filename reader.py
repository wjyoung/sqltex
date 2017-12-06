import argparse
import sys
import re


def establish_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', help='Database name', required=False)
    parser.add_argument('-f', '--sql_file', help='File containing SQL queries', required=False)
    return parser.parse_args()


def get_args():
    """
    Reads args provided and reacts accordingly.
    Not fully functional.

    :return: tuple containing database name and sql file name
    """

    args = establish_args()
    sql_file = args.sql_file if args.sql_file else raw_input('Enter .sql file to run\n')
    db = args.database if args.database else raw_input('Enter database name\n')
    return db, sql_file


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
