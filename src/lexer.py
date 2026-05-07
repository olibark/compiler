from constants import KEYWORDS, CHARTOKENS

class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.tokens = []
        self.source_len = len(source)
        assert isinstance(source, str) 
        
    def tokenize(self) -> list:
        while self.position < len(self.source):
            current_char = self.source[self.position]
            
            if current_char.isspace():
                self.position += 1
            
            elif current_char.isalpha():
                value = self.consume_identifier()
                token_type = "KEYWORD" if value in KEYWORDS else "IDENTIFIER"
                token = (token_type, value)
                self.tokens.append(token)
                
            elif current_char.isdigit():
                value = self.consume_number()
                token_type = "INT"
                token = (token_type, value)
                self.tokens.append(token)
                
            elif current_char in CHARTOKENS:
                two_char_token = current_char + (self.peek() or "")
                if two_char_token in CHARTOKENS:
                    token_type = CHARTOKENS[two_char_token]
                    token = (token_type, two_char_token)
                    self.tokens.append(token)
                    self.position += 2
                
                else: raise SyntaxError(f"Unexpected character: {current_char}")
                    
                token_type = CHARTOKENS[current_char]
                token = (token_type, current_char)
                self.tokens.append(token)
                self.position += 1
                
                
            else: raise SyntaxError(f"Unexpected character: {current_char}")
        
        self.tokens.append(("EOF", None))
        return self.tokens

    def consume_identifier(self) -> str:
        start_pos = self.position
        while self.position < self.source_len and self.source[self.position].isalnum():
            self.position += 1
            
        return self.source[start_pos:self.position]
    
    def consume_number(self) -> str:
        start_pos = self.position
        while self.position < self.source_len and self.source[self.position].isdigit():
            self.position += 1
            
        return self.source[start_pos:self.position]
    
    def peek(self):
        if self.position + 1 >= self.source_len:
            return None
        
        else: return self.source[self.position + 1]