#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Usage: flame <filetype> <op> <item> <url> [<obj>]

-h --help    show this
"""
import os

from docopt import docopt
from jinja2 import Environment, FileSystemLoader


RULES_DIR = os.path.join(os.path.dirname(__file__), 'rules')
env = Environment(loader=FileSystemLoader(RULES_DIR))


def render_api_function(**kwargs):
    template = env.get_template('rules')
    return template.render(**kwargs).strip()


if __name__ == '__main__':
    args = docopt(__doc__)
    # remove surrounding angled brackets, <arg>
    kwargs = {k[1: len(k)-1]: v for (k, v) in args.items()}
    print render_api_function(**kwargs)
