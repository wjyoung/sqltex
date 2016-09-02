import engine
import subprocess
import reader
import sys

db, file_in = reader.get_args()

if db is not None and file_in is not None:
    proc = subprocess.Popen(args=["psql", "-a", "-A", "-F", ",", "-d", db, "-f", file_in], stdout=subprocess.PIPE)
    # http://stackoverflow.com/questions/4514751/pipe-subprocess-standard-output-to-a-variable
    data = proc.stdout.read()
    engine.write_tex_file(data)
elif len(sys.argv) <= 2 and file_in is not None:
    engine.write_tex_file(file_in)
else:
    sys.stderr("Database or sql or txt not given. Program exiting")


