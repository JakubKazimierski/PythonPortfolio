'''
Zadanie 1 Lista 3
JFTT Jakub Kazimierski
based on example from ply-3.11 README.md
'''

import ply.lex as lex
import ply.yacc as yacc
import sys
import math

# below appends in reverse polish notation
listOfOperations = []

# method returns inversion of modular division
def modInverse(b,m): 
    g = math.gcd(b, m)  
    if (g != 1): 
        # print("Inverse doesn't exist")  
        return -1
    else:  
        # If b and m are relatively prime,  
        # then modulo inverse is b^(m-2) mode m  
        return pow(b, m - 2, m) 


# ---------------------------------
# list of tokens
tokens = (
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'EXP','LPAREN','RPAREN','COMMENTS',
    )

# Tokens

t_PLUS    = r'\+' 
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_EXP     = r'\^'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER(t):
    r'\d+'    
    t.value = int(t.value)
    return t

def t_COMMENTS(t):
    r'\#.*'
    t.value = ''
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lex.lex()

# Precedence rules for the arithmetic operators
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','EXP'),
    ('right','UMINUS'),
    )
    
def p_statement_expr(p):
    'statement : expression'
    
    print(p[1])

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
                    | expression MINUS expression
                    | expression TIMES expression
                    | expression DIVIDE expression
                    | expression EXP expression
    '''
    
    listOfOperations.append(p[2])
    
    if p[2] == '+'  : 
        p[0] = (p[1]%1234577 + p[3]%1234577)%1234577
    
    elif p[2] == '-': 
        p[0] = (p[1]%1234577 - p[3]%1234577)%1234577
    
    elif p[2] == '*': 
        oldVal = 0    
        for i in range(0, p[3]):
            oldVal = (p[1]+oldVal)%1234577
        p[0] = oldVal
    
    elif p[2] == '/':
        inv = modInverse(p[3],1234577)  
        p[0] = ((p[1]%1234577) * inv)%1234577
    
    elif p[2] == '^':
        oldVal = 1
        for i in range(0, p[3]):
            oldVal = (p[1]*oldVal)%1234577
        p[0] = oldVal

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'    
    p[0] = 1234577-p[2]%1234577
    listOfOperations.append("-> "+str(p[0]))

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]%1234577
    listOfOperations.append(p[0])

def p_expression_comments(p):
    'expression : COMMENTS'
    p[0] = p[1]


def p_error(p):
    print("Syntax error at '%s'" % p.value)
# ----------------------------

yacc.yacc()

print("\n[Calculator]")
print("Options: (*, /, +, -, %, variables)\n")
while True:
    # Scans for input, breaks with (CTRL + C) in the console
    try:
        s = input('>> ')
    except EOFError:
        break    
    yacc.parse(s)
    print(" ".join(str(x) for x in listOfOperations))
    listOfOperations.clear()