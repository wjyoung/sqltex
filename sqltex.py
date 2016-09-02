import sqlToTexParser
import subprocess
import sqlOutputReader
import sys

db, file_in = sqlOutputReader.get_args()

if db is not None and file_in is not None:
    proc = subprocess.Popen(args=["psql", "-a", "-A", "-F", ",", "-d", db, "-f", file_in], stdout=subprocess.PIPE)
    # http://stackoverflow.com/questions/4514751/pipe-subprocess-standard-output-to-a-variable
    data = proc.stdout.read()
    sqlToTexParser.build_tex_string(data)
elif len(sys.argv) <= 2 and file_in is not None:
    sqlToTexParser.build_tex_string(file_in)
else:
    sys.stderr("Database or sql or txt not given. Program exiting")


