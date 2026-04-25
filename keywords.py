class Keywords:
    def __init__(self):
        self.keywords = {
            "int",
            "if",
            "else",
            "while",
            "return",
            "for",
            "true",
            "false",
        }
        
    def is_keyword(self, identifier):
        return identifier in self.keywords