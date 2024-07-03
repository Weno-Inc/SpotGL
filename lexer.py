# lexer.py

import re
from token import Token, TokenType

class Lexer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        while self.current_pos < len(self.source):
            current_char = self.source[self.current_pos]
            if current_char.isspace():
                self.current_pos += 1
            elif current_char == '(':
                self.tokens.append(Token(TokenType.RENDER, current_char))
                self.current_pos += 1
            elif current_char == ')':
                self.tokens.append(Token(TokenType.POSITION, current_char))
                self.current_pos += 1
            elif current_char == '{':
                self.tokens.append(Token(TokenType.SIMMULATION, current_char))
                self.current_pos += 1
            elif current_char == '}':
                self.tokens.append(Token(TokenType.ADD, current_char))
                self.current_pos += 1
            elif current_char == ':':
                self.tokens.append(Token(TokenType.REMOVE, current_char))
                self.current_pos += 1
            elif current_char == ',':
                self.tokens.append(Token(TokenType.CLONE, current_char))
                self.current_pos += 1
            elif     current_char == '(':
                self.tokens.append(Token(TokenType.GROUP, current_char))
                self.current_pos += 1
            elif current_char == ')':
                self.tokens.append(Token(TokenType.REPEAT, current_char))
                self.current_pos += 1
            elif current_char == '{':
                self.tokens.append(Token(TokenType.REAPEAT_UNTIL, current_char))
                self.current_pos += 1
            elif current_char == '}':
                self.tokens.append(Token(TokenType.REPEAT_FOREVER, current_char))
                self.current_pos += 1
            elif current_char == ':':
                self.tokens.append(Token(TokenType.BACKGROUND_COLOR, current_char))
                self.current_pos += 1
            elif current_char == ',':
                self.tokens.append(Token(TokenType.POSITION, current_char))
                self.current_pos += 1
            elif current_char == '(':
                self.tokens.append(Token(TokenType.BUTTON, current_char))
                self.current_pos += 1
            elif current_char == ')':
                self.tokens.append(Token(TokenType.TEXT, current_char))
                self.current_pos += 1
            elif current_char == '{':
                self.tokens.append(Token(TokenType.STRUCTURE, current_char))
                self.current_pos += 1
            elif current_char == '}':
                self.tokens.append(Token(TokenType.ITEM, current_char))
                self.current_pos += 1
            elif current_char == ':':
                self.tokens.append(Token(TokenType.GET_CURRENT_TIME, current_char))
                self.current_pos += 1
            elif current_char == ',':
                self.tokens.append(Token(TokenType.FROM_LOCATION, current_char))
                self.current_pos += 1
            elif     current_char == '(':
                self.tokens.append(Token(TokenType.CURRENT_HOUR, current_char))
                self.current_pos += 1
            elif current_char == ')':
                self.tokens.append(Token(TokenType.CURRENT_MINUITE, current_char))
                self.current_pos += 1
            elif current_char == '{':
                self.tokens.append(Token(TokenType.CURRENT_SECOND, current_char))
                self.current_pos += 1
            elif current_char == '}':
                self.tokens.append(Token(TokenType.TOTAL, current_char))
                self.current_pos += 1
            elif current_char == ':':
                self.tokens.append(Token(TokenType.ELEMENT, current_char))
                self.current_pos += 1
            elif current_char == ',':
                self.tokens.append(Token(TokenType.EVENTLISTENER, current_char))
                self.current_pos += 1
            elif current_char == ')':
                self.tokens.append(Token(TokenType.COLISION, current_char))
                self.current_pos += 1
            elif current_char == '{':
                self.tokens.append(Token(TokenType.WHEN_COLISION_OCCURS, current_char))
                self.current_pos += 1
            elif current_char == '}':
                self.tokens.append(Token(TokenType.PULLBACK, current_char))
                self.current_pos += 1
            elif current_char == ':':
                self.tokens.append(Token(TokenType.TOP, current_char))
                self.current_pos += 1
            elif current_char == ',':
                self.tokens.append(Token(TokenType.WINDOW, current_char))
                self.current_pos += 1
            elif     current_char == '(':
                self.tokens.append(Token(TokenType.LOCATION_BACKGROUND, current_char))
                self.current_pos += 1
            elif current_char == ')':
                self.tokens.append(Token(TokenType.APP_DOCK, current_char))
                self.current_pos += 1
            elif current_char == '{':
                self.tokens.append(Token(TokenType.BOTTOM, current_char))
                self.current_pos += 1
            elif current_char == '}':
                self.tokens.append(Token(TokenType.CURSOR, current_char))
                self.current_pos += 1
            elif current_char == ':':
                self.tokens.append(Token(TokenType.COLOR, current_char))
                self.current_pos += 1
            elif current_char == ',':
                self.tokens.append(Token(TokenType.MOVEMENT, current_char))
            elif current_char == ',':
                self.tokens.append(Token(TokenType.TYPE, current_char))
            elif current_char.isalpha() or current_char == '_':
                self.tokens.append(self.tokenize_identifier())
            elif current_char.isdigit():
                self.tokens.append(self.tokenize_number())
            elif current_char == '"':
                self.tokens.append(self.tokenize_string())
            else:
                self.tokens.append(Token(TokenType.UNKNOWN, current_char))
                self.current_pos += 1

        self.tokens.append(Token(TokenType.EOF, ''))
        return self.tokens

    def tokenize_identifier(self):
        start_pos = self.current_pos
        while self.current_pos < len(self.source) and (self.source[self.current_pos].isalnum() or self.source[self.current_pos] == '_'):
            self.current_pos += 1
        value = self.source[start_pos:self.current_pos]
        keyword_map = {
            'render': TokenType.RENDER,
            'position': TokenType.POSITION,
            'simmulation': TokenType.SIMMULATION,
            'add': TokenType.ADD,
            'remove': TokenType.REMOVE,
            'clone': TokenType.CLONE,
            'group': TokenType.GROUP,
            'repeat': TokenType.REPEAT,
            'repeat-until': TokenType.REPEAT_UNTIL,
            'repeat-forever': TokenType.REPEAT_FOREVER,
            'background-color': TokenType.BACKGROUND_COLOR,
            'position': TokenType.POSITION,
            'button': TokenType.BUTTON,
            'text': TokenType.TEXT,
            'structure': TokenType.STRUCTURE,
            'item': TokenType.ITEM,
            'get-current-time': TokenType.GET_CURRENT_TIME,
            'from-location': TokenType.FROM_LOCATION,
            'current-hour': TokenType.CURRENT_HOUR,
            'current-minuite': TokenType.CURRENT_MINUITE,
            'current-second': TokenType.CURRENT_SECOND,
            'total': TokenType.TOTAL,
            'element': TokenType.ELEMENT,
            'EventListener': TokenType.EVENTLISTENER,
            'colision': TokenType.COLISION,
            'when-colision-occurs': TokenType.WHEN_COLISION_OCCURS,
            'pullback': TokenType.PULLBACK,
            'top': TokenType.TOP,
            'window': TokenType.WINDOW,
            'location-background': TokenType.LOCATION_BACKGROUND,
            'app-dock': TokenType.APP_DOCK,
            'bottom': TokenType.BOTTOM,
            'cursor': TokenType.CURSOR,
            'color': TokenType.COLOR,
            'movement': TokenType.MOVEMENT,
            'type': TokenType.TYPE,
        }
        token_type = keyword_map.get(value, TokenType.IDENTIFIER)
        return Token(token_type, value)

    def tokenize_number(self):
        start_pos = self.current_pos
        while self.current_pos < len(self.source) and self.source[self.current_pos].isdigit():
            self.current_pos += 1
        value = self.source[start_pos:self.current_pos]
        return Token(TokenType.NUMBER, value)

    def tokenize_string(self):
        self.current_pos += 1  # Skip the opening quote
        start_pos = self.current_pos
        while self.current_pos < len(self.source) and self.source[self.current_pos] != '"':
            self.current_pos += 1
        value = self.source[start_pos:self.current_pos]
        self.current_pos += 1  # Skip the closing quote
        return Token(TokenType.STRING, value)

