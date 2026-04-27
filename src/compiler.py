from pathlib import Path
from pprint import pformat

from parser import Parser
from ir import IRGenerator
from vm import VM

source = Path('source.txt').read_text()

program_name = "main"
build_dir = Path("out")

parser = Parser(source)
generator = IRGenerator()
vm = VM()

tokens = parser.tokens
ast = parser.parse()
instructions = generator.generate(ast)
result = vm.run(instructions)

build_dir.mkdir(exist_ok=True)

artifacts = {
    f"{program_name}.src": source + "\n",
    f"{program_name}.tok": pformat(tokens) + "\n",
    f"{program_name}.ast": pformat(ast) + "\n",
    f"{program_name}.ir": pformat(instructions) + "\n",
    f"{program_name}.output": pformat(result) + "\n",
    f"{program_name}.env": pformat(vm.env) + "\n",
}

for name, contents in artifacts.items():
    (build_dir / name).write_text(contents)

print(f"Built {program_name}")
print(f"Source: {build_dir / f'{program_name}.src'}")
print(f"Tokens: {build_dir / f'{program_name}.tok'}")
print(f"AST: {build_dir / f'{program_name}.ast'}")
print(f"IR: {build_dir / f'{program_name}.ir'}")
print(f"Output: {build_dir / f'{program_name}.output'}")
print(f"Environment: {build_dir / f'{program_name}.env'}")
