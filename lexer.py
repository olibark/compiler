from keywords import Keywords
from charTokens import CharTokens

keywords = Keywords()
charTokens = CharTokens()

class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.tokens = []
        self.source_len = len(source)        
        assert isinstance(source, str)
    
    def tokenize(self) -> None:
        while self.position < len(self.source):
            current_char = self.source[self.position]
            
            if current_char.isspace():
                self.position += 1
            
            elif current_char.isalpha():
                value = self.consume_identifier()
                token_type = "KEYWORD" if keywords.is_keyword(value) else "IDENTIFIER"
                token = (token_type, value)
                self.tokens.append(token)
                
            elif current_char.isdigit():
                value = self.consume_number()
                self.tokens.append(("INT", value))

            elif charTokens.is_char_token(current_char):
                two_char_token = current_char + (self.peek() or "")
                if charTokens.is_char_token(two_char_token):
                    self.tokens.append((charTokens.char_tokens[two_char_token], two_char_token))
                    self.position += 2
                elif charTokens.is_char_token(current_char):
                    token_type = charTokens.char_tokens[current_char]
                    self.tokens.append((token_type, current_char))
                    self.position += 1
                else: raise SyntaxError(f"Unexpected character: {current_char}")
            
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
    
    def peek(self) -> str:
        if self.position + 1 >= self.source_len:
            return None
        else: 
            return self.source[self.position + 1]
    
source = "x >= 5 + 3;"
lexer = Lexer(source)
lexer.tokenize()
print(source)
print(lexer.tokens)