from .parser import *
from .parser.ast import *
from .lexer import *

def gencode(prog_list):
    a = sorted(prog_list, key=lambda x: x.line)
    s = """
\tORG 32768
"""
    for l in a:
        s += l.codegen()
    return s

def do_all(s):
    return gencode(parse_program(lex(s.upper())))
