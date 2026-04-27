class VM:
    def __init__(self):
        self.stack = []
        self.env = {}
        
    def run(self, instructions):
        for opcode, value in instructions:
            match opcode:
                case "PUSH":
                    self.stack.append(value)
                
                case "LOAD":
                    if value not in self.env:
                        raise NameError(f"Undefined variable: {value}")
                    self.stack.append(self.env[value])
                    
                case "STORE":
                    self.env[value] = self.stack.pop()
                    
                case "PLUS" | "MINUS" | "MULTIPLY" | "SLASH" | "GT" | "LT" | "GTEQ" | "LTEQ" | "EQ" | "NEQ":
                    right = self.stack.pop()
                    left = self.stack.pop()
                    
                    match opcode:
                        case "PLUS":
                            self.stack.append(left + right)
                        
                        case "MINUS":
                            self.stack.append(left - right)
                            
                        case "MULTIPLY":
                            self.stack.append(left * right)
                            
                        case "SLASH":
                            self.stack.append(left / right)
                            
                        case "GT":
                            self.stack.append(left > right)
                            
                        case "LT":
                            self.stack.append(left < right)
                        
                        case "GTEQ":
                            self.stack.append(left >= right)
                            
                        case "LTEQ":
                            self.stack.append(left <= right)
                            
                        case "EQ":
                            self.stack.append(left == right)
                            
                        case "NEQ":
                            self.stack.append(left != right)
                            
                case _: raise ValueError(f"Unknown instruction: {opcode}")
                
        return self.stack[-1] if self.stack else None                                
                