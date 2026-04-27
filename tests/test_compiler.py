from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evaluator import Evaluator
from ir import IRGenerator
from lexer import Lexer
from parser import Parser
from vm import VM


def test_lexer_tokenizes_assignment_and_comparison():
    source = "x = 10; y = x + 5; y >= 15"

    tokens = Lexer(source).tokenize()

    assert tokens == [
        ("IDENTIFIER", "x"),
        ("ASSIGN", "="),
        ("INT", "10"),
        ("SEMI", ";"),
        ("IDENTIFIER", "y"),
        ("ASSIGN", "="),
        ("IDENTIFIER", "x"),
        ("PLUS", "+"),
        ("INT", "5"),
        ("SEMI", ";"),
        ("IDENTIFIER", "y"),
        ("GTEQ", ">="),
        ("INT", "15"),
        ("EOF", None),
    ]


def test_lexer_raises_for_unexpected_character():
    with pytest.raises(SyntaxError, match="Unexpected character: @"):
        Lexer("@").tokenize()


def test_parser_respects_operator_precedence():
    ast = Parser("1 + 2 * 3").parse()

    assert ast == (
        "PROGRAM",
        [
            (
                "PLUS",
                ("INT", "1"),
                ("MULTIPLY", ("INT", "2"), ("INT", "3")),
            )
        ],
    )


def test_parser_respects_parentheses():
    ast = Parser("(1 + 2) * 3").parse()

    assert ast == (
        "PROGRAM",
        [
            (
                "MULTIPLY",
                ("PLUS", ("INT", "1"), ("INT", "2")),
                ("INT", "3"),
            )
        ],
    )


def test_evaluator_runs_assignment_program_and_keeps_environment():
    source = "x = 10; y = x + 5; y >= 15"
    ast = Parser(source).parse()
    evaluator = Evaluator()

    result = evaluator.evaluate(ast)

    assert result is True
    assert evaluator.env == {
        "x": 10,
        "y": 15,
    }


def test_evaluator_raises_for_undefined_variable():
    with pytest.raises(NameError, match="Undefined variable: missing"):
        Evaluator().evaluate(("IDENTIFIER", "missing"))


def test_ir_generator_builds_stack_machine_instructions():
    ast = Parser("x = 10; y = x + 5; y >= 15").parse()

    instructions = IRGenerator().generate(ast)

    assert instructions == [
        ("PUSH", 10),
        ("STORE", "x"),
        ("LOAD", "x"),
        ("PUSH", 5),
        ("PLUS", None),
        ("STORE", "y"),
        ("LOAD", "y"),
        ("PUSH", 15),
        ("GTEQ", None),
    ]


def test_vm_runs_generated_instructions_and_matches_evaluator():
    source = "x = 10; y = x + 5; y >= 15"
    ast = Parser(source).parse()
    instructions = IRGenerator().generate(ast)

    evaluator = Evaluator()
    vm = VM()

    expected = evaluator.evaluate(ast)
    result = vm.run(instructions)

    assert result == expected
    assert vm.env == evaluator.env


def test_vm_raises_for_undefined_variable():
    with pytest.raises(NameError, match="Undefined variable: missing"):
        VM().run([("LOAD", "missing")])
