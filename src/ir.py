class IRGenerator:
    def generate(self, node):
        token_type = node[0]
        
        match token_type:
        
            case "PROGRAM":
                instructions = []
                for statement in node[1]:
                    instructions.extend(self.generate(statement))
                
                return instructions
        
            case "INT":
                return [("PUSH", int(node[1]))]
            
            case "IDENTIFIER":
                return [("LOAD", node[1])]
            
            case "ASSIGN":
                name = node[1]
                value = node[2]
                return self.generate(value) + [("STORE", name)]
            
            case "PLUS" | "MINUS" | "MULTIPLY" | "SLASH" | "GT" | "LT" | "GTEQ" | "LTEQ" | "EQ" | "NEQ":
                left = self.generate(node[1])
                right = self.generate(node[2])
                return left + right + [(token_type, None)]
        
            case _: 
                raise ValueError(f"Unknown AST node: {node}")
            
