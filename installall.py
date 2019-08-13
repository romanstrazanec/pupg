import os
import re
from random import randint
from multiprocessing import Process


def pip(package):
    print(f"Updating {package}")
    os.system(f"pip install -U {package}")


def cabal():
    print(f"Updating Haskell libraries")
    os.system("cabal update")


def stack():
    print(f"Upgrading Stack")
    os.system("stack update")
    os.system("stack upgrade")


def npm():
    print(f"Upgrading npm")
    os.system("npm i npm")


if __name__ == "__main__":
    CWD = os.getcwd().replace('\\', '/')
    UPDATE_FILE = f"{CWD}/updates{randint(1e5, 1e6)}.txt"

    processes = []
    os.system(f"pip list -o > {UPDATE_FILE}")
    with open(UPDATE_FILE) as f:
        for line in f.readlines():
            match = re.match(r"^[A-za-z0-9-]+", line)
            if match:
                p = Process(target=pip, args=(match.group(),))
                processes.append(p)

    os.remove(UPDATE_FILE)

    for p in processes:
        p.start()
