#!/usr/bin/python3
from argparse import ArgumentParser, Namespace as ArgNamespace
from subprocess import run as subproc, CompletedProcess, CalledProcessError
from typing import List


def get_args() -> ArgNamespace:
    parser = ArgumentParser(description='Upgrade all your python packages.')
    parser.add_argument('-l', '--limit', type=int, default=7,
                        help='set default upgrade try limit (default=7)')
    parser.add_argument('-mp', '--multiproc', action='store_true',
                        help='''use multiprocessing library to distribute
                                upgrades across multiple processes''')
    parser.add_argument('-c', '--check', action='store_true',
                        help='check if upgrade was successful')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def pip(*args) -> List[str]:
    return ['pip', *args]


def get_outdated_pckgs() -> List[str]:
    res = subproc(pip('list', '-o'), capture_output=True, text=True)
    return [line.split(' ')[0] for line in res.stdout.split('\n')[1:]]


def upgrade(pckg: str, dutl: int, ntry: int = 0) -> bool:
    if ntry == 0:
        print('Upgrading', pckg)
    try:
        subproc(pip('install', '-U', pckg), check=True)
        return True
    except CalledProcessError:
        return False if ntry == dutl else upgrade(pckg, ntry + 1, dutl)


if __name__ == "__main__":
    args = get_args()
    pckgs = get_outdated_pckgs()

    if len(pckgs) == 0:
        exit('All packages are up to date!')

    if args.multiproc:
        from multiprocessing import Process as Proc
        procs = (Proc(target=upgrade, args=(pckg, args.limit)) for pckg in pckgs)

        for p in procs:
            p.start()
    else:
        for pckg in pckgs:
            upgrade(pckg, args.limit)

    if args.check:
        print('Checking outdated packages...')
        pckgs = get_outdated_pckgs()
        if len(pckgs) == 0:
            print('All packages are up to date!')
        else:
            print('Not upgraded packages:')
            print('\n'.join(pckgs))
