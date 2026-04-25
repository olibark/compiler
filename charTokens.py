class CharTokens:
    def __init__(self):
        self.char_tokens = {
            "=": "ASSIGN",
            ";": "SEMI",
            "+": "PLUS",
            "-": "MINUS",
            "*": "MULTIPLY",
            "/": "SLASH",
            "(": "LPAREN",
            ")": "RPAREN",
            "{": "LBRACE",
            "}": "RBRACE",
            "==": "EQ",
            "!=": "NEQ",
            ">=": "GTEQ",
            "<=": "LTEQ",
            ">": "GT",
            "<": "LT"
        }
        
    def is_char_token(self, char):
        return char in self.char_tokens