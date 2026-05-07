class Evaluator:
    def __init__(self, env=None):
        self.env = env or {}
        
    def evaluate(self, node):
        token_type = node[0]
        match token_type:
            case "PROGRAM":
                result = None
                
                for statement in node[1]:
                    result = self.evaluate(statement)
            
            case "INT":
                return int(node[1])
            
            case "IDENTIFIER":
                name = node[1]
                
                if name not in self.env:
                    raise NameError(f"Undefined variable: {name}")
                
                return self.env[name]
                
            case ("PLUS" | "MINUS" | "MULTIPLY" | "SLASH" |
                  "GT" | "LT" | "GTEQ" | "LTEQ" | "EQ" | "NEQ"):

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
            
            case "KEYWORD":
                if node[1] == "true":
                    return True
                if node[1] == "false":
                    return False    
            
            case "ASSIGN":
                name = node[1]
                value = self.evaluate(node[2])
                self.env[name] = value
                
                return value
            
            case _:
                raise ValueError(f"Unknown AST node: {node}")
            