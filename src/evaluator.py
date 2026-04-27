class Evaluator:
    def __init__(self, env=None):
        self.env = env or {}
        
    def evaluate(self, node):
        token_type = node[0]
        
        if token_type == "PROGRAM":
            result = None
            
            for statement in node[1]:
                result = self.evaluate(statement)
                
            return result
        
        if token_type == "INT":
            return int(node[1])
        
        if token_type == "IDENTIFIER":
            name = node[1]
            
            if name not in self.env:
                raise NameError(f"Undefined variable: {name}")
            
            return self.env[name]
        
        if token_type in (
            "PLUS", "MINUS", 
            "MULTIPLY", "SLASH", 
            "GT", "LT", "GTEQ", 
            "LTEQ", "EQ", "NEQ"
            ):
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            
            match token_type:
                case "PLUS":
                    return left + right
                case "MINUS":
                    return left - right
                case "MULTIPLY":
                    return left * right
                case "SLASH":
                    return left / right
                case "GT":
                    return left > right
                case "LT":
                    return left < right
                case "GTEQ":
                    return left >= right
                case "LTEQ":
                    return left <= right
                case "EQ":
                    return left == right
                case "NEQ":
                    return left != right
                
        if token_type == "KEYWORD":
            if node[1] == "true":
                return True
            if node[1] == "false":
                return False
            
        if token_type == "ASSIGN":
            name = node[1]
            value = self.evaluate(node[2])
            self.env[name] = value
            return value
        
        raise ValueError(f"Unknown AST node: {node}")