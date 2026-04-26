from lexer import Lexer
        
class Parser: 
    def __init__(self, source):
        lexer = Lexer(source)
        self.tokens = lexer.tokenize()
        self.tokens_len = len(self.tokens)
        self.current_token = self.tokens[0] if self.tokens else None
        self.position = 0
        self.parsed = []
    
    def advance(self) -> None:
        if self.position < self.tokens_len - 1:
            self.position += 1
            self.current_token = self.tokens[self.position] if self.position < self.tokens_len else None
            
    def parse_factor(self) -> list:
        token = self.current_token
        if token[0] in ("INT", "IDENTIFIER"):
            self.advance()
            return token
        
        elif token[0] == "LPAREN":
            self.advance()
            expr = self.parse_expression()
            
            if self.current_token[0] != "RPAREN":
                raise SyntaxError("Expected '')")
            
            self.advance()
            return expr

        else: raise SyntaxError(f"Expected factor, got {token}")
        
    def parse_term(self) -> list:
        left = self.parse_factor()
        
        while self.current_token and self.current_token[0] in ("MULTIPLY", "SLASH"):
            operator = self.current_token
            self.advance()
            right = self.parse_factor()
            left = (operator[0], left, right)
            
        return left
    
    def parse_expression(self) -> list:
        left = self.parse_term()
        
        while self.current_token and self.current_token[0] in ("PLUS", "MINUS"):
            operator = self.current_token
            self.advance()
            right = self.parse_term()
            left = (operator[0], left, right)
            
        return left
    
    def parse_comparison(self) -> list:
        left = self.parse_expression()
        
        while self.current_token and self.current_token[0] in ("GTEQ", "LTEQ", "LT", "GT", "EQ", "NEQ"):
            operator = self.current_token
            self.advance()
            right = self.parse_expression()
            left = (operator[0], left, right)
            
        return left            
    
    def parse(self):
        return self.parse_comparison()

source = "x + 3 * 5 >= 20"
parser = Parser(source)

print(f"Source: {source}")
print(f"Tokensized: {parser.tokens}")
print(f"Parsed: {parser.parse()}")