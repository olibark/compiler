from parser import Parser
from evaluator import Evaluator

source = "x = 10; y = x + 5; y >= 15"
parser = Parser(source)
evaluator = Evaluator()

tokenized = parser.tokens
ast = parser.parse()
evaluated = evaluator.evaluate(ast)

print(f"Source: {source}")
print(f"Tokensized: {tokenized}")
print(f"Parsed/AST: {ast}")
print(f"Evaluated: {evaluated}")