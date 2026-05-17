import sys
from pyflags.flag import Flags

def cli() -> Flags:
    flag = Flags()
    flag.add(["--ignore"], "List any files or folders to ignore", list[str], default=[".git", "venv"])
    flag.parse(sys.argv[1:])

    return flag