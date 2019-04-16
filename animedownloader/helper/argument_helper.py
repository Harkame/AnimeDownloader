import argparse
import os

from argparse import RawTextHelpFormatter

def get_arguments(arguments):
    argument_parser = argparse.ArgumentParser(description='Script to download mangas from JapScan',
    formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))

    argument_parser.add_argument(
        '-c', '--config_file',
        help = 'Set config file' + os.linesep + 'Example : python japscandownloader/main.py -c /home/myconfigfile.yml',
        type = str
    )

    argument_parser.add_argument(
        '-d', '--destination_path',
        help = 'Set destination path of downloaded mangas' + os.linesep + 'Example : python japscandownloader/main.py -d /home/mymangas/',
        type = str,
    )

    argument_parser.add_argument(
        '-v', '--verbose',
        help = 'Active verbose mode, support different level' + os.linesep + 'Example : python japscandownloader/main.py -vv',
        action = 'count',
    )

    argument_parser.add_argument(
        '-C', '--chrome',
        help = 'Use chrome (Default : firefox)' + os.linesep + 'Example : python japscandownloader/main.py -C',
        type = str,
    )

    return argument_parser.parse_args(arguments)
