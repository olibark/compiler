from parser import Parser
from evaluator import Evaluator

source = "x > 5 >= 3"
parser = Parser(source)
evaluator = Evaluator({"x": 10})

tokenized = parser.tokens
ast = parser.parse()
evaluated = evaluator.evaluate(ast)

print(f"Source: {source}")
print(f"Tokensized: {tokenized}")
print(f"Parsed/AST: {ast}")
print(f"Evaluated: {evaluated}")

