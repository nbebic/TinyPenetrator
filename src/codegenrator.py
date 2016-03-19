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
plot_xy:
\tpush	af
\tpush	bc
\tpush	hl
\tld	a,b
\tcall	calc_y_addr
\tld	a,c
\tand	%11111000
\tsrl	a
\tsrl	a
\tsrl	a
\tor	l
\tld	l,a
\tld	a,c
\tand	%00000111
\tld	b,%10000000
_pixel_shift:
\tcp	0
\tjr	z,_shift_done	
\tsrl	b
\tdec	a
\tjr	_pixel_shift
_shift_done:
\tld	a,b
\tor	(hl)
\tld	(hl),a	
\tpop	hl
\tpop	bc
\tpop	af
\tret	
calc_y_addr:
\tld	hl,$4000
\tpush	af
\tand	%00000111
\tor	h
\tld	h,a
\tpop	af
\tpush	af
\tand	%00111000
\tsla	a
\tsla	a
\tor	l
\tld	l,a
\tpop	af
\tpush	af
\tand	%11000000
\tsrl	a
\tsrl	a
\tsrl	a
\tor	h
\tld	h,a
\tpop	af
\tret



; multiplies A with 10 and puts result into A 
mult_10:
    ld IX,temp_memory
    ld (IX+1),A 
    ld (IX+2),A 
    
    sla (IX+1)
    sla (IX+1)
    sla (IX+1)

    sla (IX+2)
    sla (IX+2)

    ld A,0
    ADD a,(IX+1)
    ADD A,(IX+2)
    RET

; Gets current key (or waits for it) and puts it into memory on address HL and increases HL 
input:
\tld de, 0
.wait_key:
\thalt
\tLD A,(23611)
\tAND %00100000
\tJP Z,.wait_key
\tLD A,(23611)
\tAND %11011111
\tLD (23611), A
\tLD A,(23560)
\tLD (buffer),A
\tld hl, buffer
\tpush af
\tpush de
\tcall print_str
\tpop de
\tpop af
\tCP 13
\tJP Z,.enter
\tsub 48
\tld hl, 0
\tadd hl, de
\tadd hl, hl
\tld b, h
\tld c, l
\tadd hl, hl
\tadd hl, hl
\tadd hl, bc
\tld b, 0
\tld c, a
\tadd hl, bc
\tld d, h
\tld e, l
\tjp .wait_key
.enter:
\tld b, d
\tld c, e
\tret
buffer: DB 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
temp_memory: DB 0,0,0,0,0,0,0,0,0,0
input_number: DB 0,0,0,0,0,0,0
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
