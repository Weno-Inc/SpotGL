# main.py

from lexer import Lexer

if __name__== '__main__':
    source_code = 'EventListner when-collision-occurs pullback'
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)