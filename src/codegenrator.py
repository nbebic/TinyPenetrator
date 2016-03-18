from .parser import *
from .parser.ast import *
from .lexer import *

def gencode(prog_list):
    a = sorted(prog_list, key=lambda x: x.line)
    s = """
\tORG 32768
\tjp main
print_str:
\tld a, (hl)
\tor a
\tjp z, .end
.loop:
\tpush hl
\tcall $0AD9
\tpop hl
\tinc hl
\tld a, (hl)
\tor a
\tjp nz, .loop
.end:
\tret

print_num:
\tcall $2D2B
\tcall $2DE3
\tret

main:
"""
    for l in a:
        s += l.codegen()
    s += '\nvars: rw 26\n'
    return s

def do_all(s):
    return gencode(parse_program(lex(s.upper())))
