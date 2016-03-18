from .parser import *
from .parser.ast import *
from .lexer import *

def gencode(prog_list):
    a = sorted(prog_list, key=lambda x: int(x.line))
    s = """
\tORG 32768
\tld a, 2
\tcall 5633
\tjp main
print_str:
\tld a, (hl)
\tor a
\tjp z, .end
.loop:
\tpush hl
\tcall $09F4
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

mult_de_bc
\tld hl, 0

\tsla  e	\t; optimised 1st iteration
\trl d
\tjr nc, $+4
\tld h, b
\tld l, c

\tld a, 15
_mult_loop:
\tadd  hl, hl
\trl e
\trl d
\tjr nc, $+6
\tadd hl, bc
\tjr nc, $+3
\tinc de
\t
\tdec a
\tjr nz, _mult_loop
\t
\tret

div_hl_c:
\txor a
\tld b, 16

_div_loop:
\tadd hl, hl
\trla
\tcp c
\tjr c, $+4
\tsub c
\tinc l
\t
\tdjnz _div_loop
\t
\tret


main:
"""
    for l in a:
        s += l.codegen()
    s += '\nvars: dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n'
    for constant in CONSTANTS_CODE:
        s += constant
    return s

def do_all(s):
    return gencode(parse_program(lex(s.upper())))
