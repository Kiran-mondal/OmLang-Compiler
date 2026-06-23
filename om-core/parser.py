# =====================================================================
# MODULE: parser.py (GRAMMATICAL PARSING & AST ENGINE)
# =====================================================================
import sys
# Note: In a multi-file layout, you would do: from lexer import TokenType
# For step-by-step assembly, we assume TokenType is available globally.

# --- Abstract Syntax Tree (AST) Storage Components ---
class AssignNode:
    def init(self, name, value):
        self.name = name
        self.value = value

class ShowNode:
    def init(self, expr):
        self.expr = expr

class BinOpNode:
    def init(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumNode:
    def init(self, val):
        self.val = val

class VarNode:
    def init(self, name):
        self.name = name

# --- The Grammatical Parser Engine ---
class OmParser:
    def init(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def consume(self, token_type):
        """Validates current token against the grammar rule and moves forward."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            print(f"Syntax Error: Expected structural token type '{token_type}', but found '{self.current_token.type}'")
            sys.exit(1)

    def parse(self):
        """Main compilation entry point loop."""
        statements = []
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.SHOW:
                self.consume(TokenType.SHOW)
                statements.append(ShowNode(self.expr()))
            elif self.current_token.type == TokenType.IDENTIFIER:
                name = self.current_token.value
                self.consume(TokenType.IDENTIFIER)
                self.consume(TokenType.ASSIGN)
                statements.append(AssignNode(name, self.expr()))
            else:
                print(f"Syntax Error: Invalid global statement start token '{self.current_token.value}'")
                sys.exit(1)
        return statements

    def expr(self):
        """Processes lower precedence operations (Addition and Subtraction)."""
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token.type
            self.consume(self.current_token.type)
            node = BinOpNode(node, op, self.term())
        return node

    def term(self):
        """Processes higher precedence operations (Multiplication and Division)."""
        node = self.factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            op = self.current_token.type
            self.consume(self.current_token.type)
            node = BinOpNode(node, op, self.factor())
        return node

    def factor(self):
        """Processes atomic base constants or isolated data structures."""
        t = self.current_token
        if t.type == TokenType.NUMBER:
            self.consume(TokenType.NUMBER)
            return NumNode(t.value)
        elif t.type == TokenType.IDENTIFIER:
            name = t.value
            self.consume(TokenType.IDENTIFIER)
            return VarNode(name)
            
        print(f"Parser Error: Unexpected mathematical layout expression factor token '{t}'")
        sys.exit(1)