#!/usr/bin/env python
import os
import sys
import json
import pathlib
import logging
from logging.handlers import RotatingFileHandler
import argparse

path = pathlib.Path(__file__).parent
LOGFILE = path.parent/'.log'

## Default loggers
## console
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(message)s'))
logging.getLogger().addHandler(console)
## File rotation in path/logs/
logfile = RotatingFileHandler(LOGFILE, maxBytes=2000, backupCount=10)
logfile.setLevel(logging.INFO)
logfile.setFormatter(logging.Formatter('%(asctime)s %(name)-s %(levelname)-8s %(message)s'))
logging.getLogger().addHandler(logfile)


def argparse_wrapper(default_args, help_dict=None, description=None, usage=None, argv=sys.argv, out_dict=True):
    """Parses script arguments to customize values of `default_args` dictionnary

    Wraps `argparse` to return an update version of the provided `default_args` 
    with the values passed to the script from the command prompt. For example,
    using this function in the file `foo.py` with `default_args={'foo':0, 'bar':
    [1,2,3], 'boo': True, 'far': None} would immediately allow to prompt

        python foo.py --foo 23 --bar 4 5 6 7 --far my_str --no_boo 

    The function also support passing a file to the script to read args from a 
    `.json` file, for example

        python foo.py params.json --bar 7 8 9

    The parameters priority is script args first, json file second, and default 
    dict otherwise.

    Args:
    - default_args (dict): dictionnary of the default parameters
    - help_dict (dict, optional): helpstrings for --help. Defaults to None.
    - description (str, optional): short --help description. Defaults to None.
    - usage (str, optional): long --help description. Defaults to None.
    - argv (list, optional): manual scripts arguments. Defaults to sys.argv.
    - out_dict (bool, optional): output dict or Namespace. Defaults to True.

    Returns:
    - dict: dictionnary of the parameters read from the command prompt
    """
    if argv is None: 
        argv=sys.argv
        
    if len(argv)>1 and not (argv[1] == "--help" or argv[1] == "-h"):
        filename = argv[1] 
        if filename[-5:]=='.json':
            if os.path.exists(filename):
                with open(filename) as f:
                    params_dict = json.load(f)
                print(f'using parameters from file {filename}')
            else: raise ValueError(f'file {filename} not found')
        else: print('using default parameters with args')
    else: print('using default parameters')

    parser = argparse.ArgumentParser(description=description, usage=usage)
    for name, default in default_args.items():
        try: 
            helpstr = help_dict[name]
        except (KeyError, NameError, TypeError): 
            helpstr = ""

        if type(default) is list:
            parser.add_argument("--"+name, nargs="+", type=type(default[0]), default=default, help=helpstr)
        elif type(default) is bool and default is True:
            parser.add_argument("--no_"+name, dest=name, action="store_false", help=helpstr)
        elif type(default) is bool and default is False:
            parser.add_argument("--"+name, dest=name, action="store_true", help=helpstr)
        elif default is None:
            parser.add_argument("--"+name, default=default, help=helpstr)
        else:
            parser.add_argument("--"+name, type=type(default), default=default, help=helpstr)

    if out_dict: 
        return vars(parser.parse_known_args(argv)[0])
    else: 
        return parser.parse_known_args(argv)[0]