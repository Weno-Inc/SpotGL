from enum import Enum, auto

class TokenType(Enum):
    RENDER = auto()
    POSITON = auto()
    SIMMULATION = auto()
    ADD = auto()
    REMOVE = auto()
    CLONE = auto()
    GROUP = auto()
    REPEAT = auto()
    REPEAT_UNTIL = auto()
    REPEAT_FOREVER = auto()
    BACKGROUND_COLOR = auto()
    POSITION = auto()
    BUTTON = auto()
    TEXT = auto()
    STRUCTURE = auto()
    ITEM = auto()
    GET_CURRENT_TIME = auto()
    FROM_LOCATION = auto()
    CURRENT_HOUR = auto()
    CURRENT_MINUITE = auto()
    CURRENT_SECOND = auto()
    TOTAL = auto()
    ELEMENT = auto()
    EVENTLISTENER = auto()
    COLISION = auto()
    WHEN_COLISION_OCCURS = auto()
    PULLBACK = auto()
    TOP = auto()
    WINDOW = auto()
    LOCATION_BACKGROUND = auto()
    APP_DOCK = auto()
    BOTTOM = auto()
    CURSOR = auto()
    COLOR = auto()
    MOVEMENT = auto()
    TYPE = auto()

    class Token:
        def __init__(self, type, value):
            self.type = type
            self.value = value

            def __repr__(self):
                return f'Token({self.type}, {repr(self.value)})'