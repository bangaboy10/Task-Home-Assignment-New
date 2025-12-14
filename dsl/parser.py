
from lark import Lark
from .ast_builder import ASTBuilder

with open("dsl/grammar.lark") as f:
    grammar = f.read()

parser = Lark(grammar, parser="lalr", transformer=ASTBuilder())

def parse_dsl(text):
    return parser.parse(text)   
