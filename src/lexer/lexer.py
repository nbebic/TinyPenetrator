
def lex(input: str):
    tokens = []
    curtoken = ''
    curtype = ''
    for c in input + ' ':
        if curtype == 'string' and c != '"':
            curtoken += c
        elif c in '0123456789':
            if curtype != 'num':
                tokens.append(curtoken)
                curtype = 'num'
                curtoken = ''
            curtoken += c
        elif c in ' \t\r':
            if curtype != '':
                tokens.append(curtoken)
                curtype = ''
                curtoken = ''
        elif c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            if curtype != 'word':
                tokens.append(curtoken)
                curtype = 'word'
                curtoken = ''
            curtoken += c
        elif c in '<>=':
            if curtype != 'relop':
                tokens.append(curtoken)
                curtype = 'relop'
                curtoken = ''
            curtoken += c
        elif c == '"':
            if curtype == 'string':
                tokens.append('"' + curtoken + '"')
                curtype = ''
                curtoken = ''
            else:
                tokens.append(curtoken)
                curtype = 'string'
                curtoken = ''
        else:
            if curtype != '':
                tokens.append(curtoken)
                curtype = ''
                curtoken = ''
            tokens.append(c)
    while '' in tokens:
        tokens.remove('')
    return tokens

if __name__ == '__main__':
    print(lex('2 3+7 "ma + ()gija" (2+3*4) LET S = X'))