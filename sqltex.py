import argparse
import engine
import subprocess
import sys


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


def main():
    db, file_in = get_args()

    if db is not None and file_in is not None:
        # http://stackoverflow.com/questions/4514751/pipe-subprocess-standard-output-to-a-variable
        proc = subprocess.Popen(args=["psql", "-a", "-A", "-F", ",", "-d", db, "-f", file_in], stdout=subprocess.PIPE)
        data = proc.stdout.read()
        engine.write_tex_file(data)
    elif len(sys.argv) <= 2 and file_in is not None:
        engine.write_tex_file(file_in)
    else:
        sys.stderr("Database or sql or txt not given. Program exiting")


if __name__ == '__main__':
    main()
