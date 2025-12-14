# dsl/ast_builder.py
from lark import Transformer

class ASTBuilder(Transformer):

    def start(self, items):
        ast = {}
        for item in items:
            ast.update(item)
        return ast

    def entry(self, items):
        return {"entry": items[0]}

    def exit(self, items):
        return {"exit": items[0]}

    def and_op(self, items):
        return {
            "type": "logical_op",
            "op": "AND",
            "left": items[0],
            "right": items[1]
        }

    def or_op(self, items):
        return {
            "type": "logical_op",
            "op": "OR",
            "left": items[0],
            "right": items[1]
        }

    def condition(self, items):
        return {
            "type": "condition",
            "left": items[0],
            "op": items[1],
            "right": items[2]
        }

    def field(self, items):
        return {"type": "series", "value": str(items[0])}

    def indicator(self, items):
        return {
            "type": "indicator",
            "name": str(items[0]).lower(),
            "params": [items[1]["value"], int(items[2])]
        }

    def NUMBER(self, token):
        return int(token)

    def COMP(self, token):
        return str(token)
